import os
import logging
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
            position = commands.load_json(f"saves/{self.save}/state.json")
            if position is None:
                raise ValueError("Failed to load position from state.json")
            
            turn = position.get("turn", 0)
            point = position.get("point", 0)
            
            start_directory = os.path.join("domains", "testing", "starting_data")
            generate_directory = os.path.join("saves", self.save, "testing")
            
            if turn == 0 or not os.path.exists(generate_directory):
                commands.create_directory(generate_directory)
            
            turns = 5 - turn
            logging.info(f"Starting generation process with {turns} turns.")
            
            generate = TurnedGenerate(
                run_for_turns = turns, 
                directory     = generate_directory, 
                source        = start_directory, 
                prompt        = "prompt",
                turn          = turn,
                point         = point
                )
            generate.main()
            logging.info("Generation process completed successfully.")
        except Exception as e:
            logging.error(f"Error during generation process: {e}")