import os
import logging
import src.commands as commands
from domains.second.run_turn import Turn

logging.basicConfig(level=logging.INFO)

def get_input(preface):
    thing = input(f"\n{preface}: ")
    print()
    return thing

class run:
    
    def __init__(self, save):
        self.save = save
        self.load_settings()
        self.main()

    def load_settings(self):
        self.config = commands.load_json("domains/second/config.json")
        self.details = commands.load_json("domains/second/details.json")    
        
    def main(self):
        try:
            position = commands.load_json(f"saves/{self.save}/state.json")
            if position is None:
                raise ValueError("Failed to load position from state.json")
            
            self.generate_directory = os.path.join("saves", self.save, "logs")
            
            if not os.path.exists(self.generate_directory):
                commands.create_directory(self.generate_directory)
                is_turn_0 = True
            else:
                commands.create_directory(self.generate_directory)
                is_turn_0 = False
            
            turns_remaining = self.config['turn_count'] - self.config['turn']
            logging.info(f"Starting generation process with {turns_remaining} turns.")
            self.run_turns(turns_remaining, is_turn_0)
            
        except Exception as e:
            logging.error(f"Error during generation process: {e}")
            
    def run_turns(self, turns, is_turn_0):
        for current_turn in range(turns):   
            if is_turn_0:
                turn = Turn(current_turn, "domains/second/starting_data", self.generate_directory, self.config['starting_data'], self.config, self.details)
                is_turn_0 = False
            else:
                last_turn = current_turn - 1
                last_turn_path = os.path.join(self.generate_directory, f"turn_{last_turn}.json")
                
                if os.path.exists(last_turn_path):
                    turn = Turn(current_turn, last_turn_path, self.generate_directory, self.config, self.details)
                else:
                    logging.error("Error, save data corruption.")
                    break