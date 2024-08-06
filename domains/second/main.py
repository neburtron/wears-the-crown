import os
import logging
# Make new script for this one + go back to first later / just delete it
from scripts.generation import TurnedGenerate
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
            
            generate_directory = os.path.join("saves", self.save, "testing")
            
            if self.config.turn == 0 or not os.path.exists(generate_directory):
                commands.create_directory(generate_directory)
            
            turns = self.config.turn_count - self.config.turn
            logging.info(f"Starting generation process with {turns} turns.")
            
            generate = TurnedGenerate(
                run_for_turns = turns,  # gonna change
                directory     = generate_directory, 
                source        = self.config.starting_data, 
                prompt        = self.config.prompt,
                turn          = self.config.turn,
                point         = self.config.point
                )
            generate.main()
            logging.info("Generation process completed successfully.")
        except Exception as e:
            logging.error(f"Error during generation process: {e}")