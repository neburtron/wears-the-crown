import os
import logging
import random
from src.llm_interface import LLMInterface
import src.commands as commands
from src.array_manager import ArrayManager

logging.basicConfig(level=logging.INFO)
class TurnedGenerate:
    def __init__(self, run_for_turns, directory, source, prompt, turn, point):
        self.run_for_turns = run_for_turns
        self.source = source
        self.directory = directory
        self.prompt = prompt
        self.turn = turn
        self.point = point

        if not os.path.exists(self.source):
            raise FileNotFoundError(f"Save path '{self.source}' does not exist.")
        
    def main(self):
        for current_turn in range(self.run_for_turns):
            last_turn_path = self.source if self.turn == 0 else os.path.join(self.directory, str(self.turn))
            next_turn_path = os.path.join(self.directory, str(self.turn + 1))
            
            generate = Generate(source=self.source, prompt=self.prompt, directory=self.directory)
            generate.manage_items(last_turn_path, next_turn_path)

    def save_state(self):
        state = {
            "turn": self.turn,
            "point": self.point
        }
        commands.save_json(f"{self.directory}/state.json", state)
class Generate:
    
    def __init__(self, directory, source, prompt):
        self.file_num = 0
        self.current_state = ""
        self.instruct = commands.read_txt(f"prompts/{prompt}.txt")
        self.source = source
        self.directory = directory
        self.manager = ArrayManager()
        
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
        
        self.manager.clear()
        
        self.manager.input_many([
            ("system", self.instruct),
            ("user",  self.current_state),
            ("user", content)
            ])

        # 50% chance held prompt replaced by current one
        if random.random() > 0.5:
            self.current_state = content
                            
        self.call_llm(self.manager.array, previous_state, content)
            
    def call_llm(self, conversation, previous_state, content):
        try:
            instance = LLMInterface()
            response = instance.get_response(conversation)
            self.deal_with_response(response)
        except Exception as e:
            logging.error(f"During LLM interaction: {e}")
            
    def deal_with_response(self, response):
        self.single_response(response, self.file_num)
        self.file_num += 1

    def single_response(self, response, name):
        response_content = response.content if response else ""
        
        self.manager.input("assistant", response_content)
        self.manager.print()
        
        commands.save_json(f"{self.output_path}/{name}", response_content)

        source = os.path.join(self.output_path, "source")
        commands.save_json(f"{source}/{name}", self.manager)