import src.utils as utils
from llm.llm_interface import LLMInterface

class talk:
    
    def __init__(self, prompt):
        self.array = []
        self.prompt = prompt
        self.add_prompt()
        
        self.llm = LLMInterface()
        
    def add_item(self, thing, character, msg):
    
        if character:
            self.array.append({"role": thing, "content": character + ": " + msg})
        else:
            self.array.append({"role": thing, "content": msg})
        
        
    def add_prompt(self):
        message = utils.load_json(self.prompt)
        self.add_item("System", None, message)
        
    def get_response(self):
        response = self.llm.get_response(self.array)
        
        
    