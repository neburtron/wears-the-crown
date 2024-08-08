import os
import logging
import scripts.second as second
import src.commands as commands

logging.basicConfig(level=logging.INFO)

def get_input(preface):
    thing = input(f"\n{preface}: ")
    print()
    return thing

class run:
    
    def __init__(self, save):
        self.load_settings()
        self.save = save
        self.main()

    def load_settings(self):
        self.config = commands.load_json
        self.details = commands.load_json        
        
    def main(self):
        try:
            position = commands.load_json(f"saves/{self.save}/state.json")
            if position is None:
                raise ValueError("Failed to load position from state.json")
            
            self.generate_directory = os.path.join("saves", self.save, "logs")
            
            if os.path.exists(self.generate_directory):
                commands.create_directory(self.generate_directory)
                is_turn_0 = False
            else:
                commands.create_directory(self.generate_directory)
                is_turn_0 = True
            
            turns = self.config.turn_count - self.config.turn
            logging.info(f"Starting generation process with {turns} turns.")
            self.turns(turns, is_turn_0)
            
        except Exception as e:
            logging.error(f"Error during generation process: {e}")
            
    def turns(self, turns, is_turn_0):
        for turn in turns:   
            if is_turn_0:
                turn.run(turn, self.config.starting_data)
                is_turn_0 = False
            else:
                last_turn = turn - 1
                if os.path.exists(os.path.join(self.generate_directory, last_turn)):
                    turn.run(turn, 
                             os.path.join(self.generate_directory, last_turn),
                             os.path.join(self.generate_directory),
                             self.config,
                             self.details
                             )
                else:
                    print("error, save data corruption.")

class turn:

    def run(self, turn, source, root, config, details):
        self.config = config
        self.details = details
        
        self.setup_turn(turn, source, os.path.join(root, turn))
        instructions = os.path.join(root, details.get("instructions"))
        task = commands.load_json(instructions)
        self.generate(task)
        
        files = os.listdir(source)
        if os.path.exists(files):
            commands.load_json(os.path.join(root, "") )
            
        else:
            return "Error, starting data not there"
        
        
    def setup_turn(self, turn, source, path):
        os.mkdir(os.path.join(path, turn))
        # File structure for output / info storage setup
        
        
    def generate(self, task):
        return
        # will call self.hand_off for all the different types of stuff
        
        
    def hand_off(self, items, operation):
        """
        The idea is, for each opperation type, go through the list + feed to script
        I didn't write the script, this domain's a WIP. 
        """
        
        if operation == "agent":
            for item in operation:
                second.agent(item, task)
        
        elif operation == "event":
            for item in operation:
                second.event(item, task.get(item))
        