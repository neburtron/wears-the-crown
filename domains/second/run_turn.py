import os
import src.commands as commands
import scripts.second as second

class Turn:

    def __init__(self, turn, source, root, config, details):
        self.config = config
        self.details = details
        
        turn_path = os.path.join(root, f"turn_{turn}")
        self.setup_turn(turn, source, turn_path)
        
        instructions = os.path.join(root, details.get("instructions"))
        task = commands.load_json(instructions)
        self.generate(task)
        
        if os.path.exists(source):
            files = os.listdir(source)
            for file in files:
                # Add logic to handle files if necessary
                pass  # Placeholder for handling files
        else:
            return "Error, starting data not there"
        
        
    def setup_turn(self, turn, source, path):
        os.makedirs(path, exist_ok=True)
        # Ensure the directory exists and handle setup logic here
        
        
    def generate(self, task):
        if not task:
            return "No tasks found."
        
        for operation, items in task.items():
            self.hand_off(items, operation)
        
        
    def hand_off(self, items, operation):
        if operation == "agent":
            for item in items:
                second.agent(item, self.config)
        
        elif operation == "event":
            for item in items:
                second.event(item, self.config.get(item))