from LLM.llm_interface import LLMInterface
import logging
import src.commands as commands
import logging


logging.basicConfig(level=logging.INFO)

def call_llm(conversation):
    try:
        instance = LLMInterface()
        return(instance.get_response(conversation))
    except Exception as e:
        logging.error(f"During LLM interaction: {e}")

def generate(conversation, output, name):
    input = commands.load_json(conversation)
    call_llm(input)
    commands.save_json(name, output)

def generate_many(array):
    for conversation, output, name in array:
        generate(conversation, output, name)
        
class GenerationManager:
    """
    stores info to be fed to llm
    conversation - whatever the LLM is given to work with - prompt + whatever else in format LLM gets
    output - the place the generated text is to be stored (the folder)
    name - the name of the file the new text is put in
    
    Array manager is for 1 conversation W various messages 
    this is for a list of conversation json files
    """
    def __init__(self):
        self.array = []
        
    def input(self, conversation, output, name):
        self.array.append({conversation, output, name})
        
    def input_many(self, array):
        for conversation, output, name in array:
            self.array.append({conversation, output, name})

    def clear(self):
        self.array = []
        
