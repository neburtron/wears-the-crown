from operator import is_
import os
import logging
# Make new script for this one + go back to first later / just delete it
import scripts.simple as simple
import src.commands as commands

logging.basicConfig(level=logging.INFO)

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
            position = commands.load_json(f"{self.save}/state.json")
            if position is None:
                raise ValueError("Failed to load position from state.json")
            
            self.generate_directory = os.path.join("saves", self.save, "testing")
            
            if self.config.turn == 0 or not os.path.exists(self.generate_directory):
                commands.create_directory(self.generate_directory)
                is_turn_0 = True
            else:
                is_turn_0 = False
            
            turns = self.config.turn_count - self.config.turn
            logging.info(f"Starting generation process with {turns} turns.")
            self.turns(turns, is_turn_0)
            
        except Exception as e:
            logging.error(f"Error during generation process: {e}")
            
    def turns(self, turns, is_turn_0):
        for turn in turns:   
            if is_turn_0:
                self.turn(turn, self.config.starting_data)
                is_turn_0 = False
            else:
                self.turn(turn, self.generate_directory )
            
    def turn(self, turn, start_folder):
        thing = []
        i = 0
        
        files = os.listdir(start_folder)
        
        for file in files:
            thing.append({file, os.path.join(self.generate_directory, turn), f"{i}.txt", } )
            
            i += 1
        
        simple.generate_many(files)
