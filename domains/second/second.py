import src.commands as commands
import scripts.simple as simple
from LLM.llm_interface import LLMInterface

class llm:
    
    def __init__(self, prompts):
        self.prompts = commands.list(prompts)
        self.loaded_prompts = {}
        for prompt in prompts:
            self.loaded_prompts[prompt] = commands.load_json(f"{self.prompts}/{prompt}")
        self.array = []
        self.interface = LLMInterface()
        self.interface.initialize_client()
        
    def converse1(self, item, config):
        return

    def converse2(self, item, config):
        return

    def interpret(self, item, config):
        return

    def outcomes(self, item, config):
        return

    def plan(self, item, config):
        return

    def summarize(self, item, config):
        return
    
    def clear(self):
        self.array.clear