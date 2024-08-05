import os
import logging
import random
from src.llm_interface import LLMInterface
import src.commands as commands

logging.basicConfig(level=logging.INFO)

class TurnedGenerate:
        
    def __init__(self, run_for_turns, directory, source, prompt):
        self.run_for_turns = run_for_turns
        self.source = source
        self.directory = directory
        self.prompt = prompt

        if not os.path.exists(self.source):
            raise FileNotFoundError(f"Save path '{self.source}' does not exist.")
        
    def main(self):
        for turn in range(self.run_for_turns):
            last_turn_path = self.source if turn == 0 else os.path.join(self.directory, str(turn) )
            next_turn_path = os.path.join(self.directory, str(turn + 1))            
            
            generate = Generate(source=self.source, prompt=self.prompt, directory=self.directory)
            generate.manage_items(last_turn_path, next_turn_path)    

class Generate:
    
    def __init__(self, directory, source, prompt):
        self.file_num = 0
        self.current_state = ""
        self.instruct = commands.read_txt(f"prompts/{prompt}.txt")
        self.source = source
        self.directory = directory
        
        if not os.path.exists(self.source):
            raise FileNotFoundError(f"Error: Data source path '{self.source}' does not exist.")

    def manage_items(self, source, output_path):
        self.output_path = output_path
        if not os.path.exists(source):
            logging.error(f"Directory '{source}' does not exist. Skipping turn.")
            return
        
        os.makedirs(output_path, exist_ok=True)  # Ensure the output directory exists

        for item in os.listdir(source):
            item_path = os.path.join(source, item)
            if os.path.isfile(item_path):
                content = commands.read_txt(item_path)
                self.generate(content)

    def generate(self, content):
        previous_state = self.current_state
        
        if not self.current_state:
            self.current_state = content
            
        conversation = [
            {"role": "system", "content": self.instruct},
            {"role": "user", "content": self.current_state},
            {"role": "user", "content": content}
        ]

        # 50% chance held prompt replaced by current one
        if random.random() > 0.5:
            self.current_state = content
            
        logging.info(f"\n\nSystem: {self.instruct}\n\n\nUser1: {self.current_state}\n\nUser2: {content}\n\n")
        
        try:
            instance = LLMInterface()
            response = instance.get_response(conversation)
            self.deal_with_response(response, previous_state, content)
        except Exception as e:
            logging.error(f"During LLM interaction: {e}")
            
    def deal_with_response(self, response, previous_state, current_content):
        
        logging.info(f"\nResponse: {response}\n")

        response_content = response.content if response else ""

        # Save raw output 
        save_response(self.output_path, response_content, self.file_num)

        # Save raw output + inputs
        source = os.path.join(self.output_path, "source")
        os.makedirs(source, exist_ok=True)
                
        combined_content = f"{previous_state}\n\n{current_content}\n\n\n\n\n{response_content}\n"
        save_response(source, combined_content, self.file_num)        
        self.file_num += 1

def save_response(output_path, response, file_name):
    os.makedirs(output_path, exist_ok=True)
    file_path = os.path.join(output_path, f"{file_name}.txt")    
    commands.save_txt(file_path, response)
    
