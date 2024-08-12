import os
import src.commands as commands
from domains.second.second import llm

class Turn:

    def __init__(self, turn, source, root, config, details):
        self.interface = llm(os.path.join(source, "prompts"))
        self.config = config
        self.details = details
        self.turn = turn
        
        self.source = os.path.join(source, "world")
        self.turn_path = os.path.join(root, f"turn_{turn}")
        
        instructions = os.path.join(root, details.get("instructions"))        
        self.setup_turn()
        
    def setup_turn(self):
        os.makedirs(self.turn_path, exist_ok=True)
        for region in commands.list(self.source):
            region_path = os.path.join(self.turn_path, region)
            os.makedirs(region_path, exist_ok=True)
            for thing in os.listdir(os.path.join(self.source, region)):
                self.generate(thing, region_path)
                
    def generate(self, thing, path): 
        prompt = commands.load_json(task)
        output = self.hand_off(thing, prompt)
        commands.save_json(output, os.path.join(path, thing))
        
    def hand_off(self, items, operation):
        if operation == "converse1":
            for item in items:
                self.interface.converse1(item, self.config)
        elif operation == "converse2":
            for item in items:
                self.interface.converse2(item, self.config.get(item))
        elif operation == "interpret":
            for item in items:
                self.interface.interpret(item, self.config.get(item))
        elif operation == "outcomes":
            for item in items:
                self.interface.outcomes(item, self.config.get(item))
        elif operation == "plan":
            for item in items:
                self.interface.plan(item, self.config.get(item))
        elif operation == "summarize":
            for item in items:
                self.interface.summarize(item, self.config.get(item))