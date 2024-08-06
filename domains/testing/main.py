"""
Working on modularity / the framework of it all + making this usable.

This used to be hardcoded, now it's a step towards plug and play

Domains implementation is a WIP, project root dir main.py is going to be changed when I'm not exhausted.

structure / whatever:
----------------------
Starting conditions folder W txt files in it
Special cycles folder - maybe
terminal_interface script - handles user interface / the thing that handles the order things are called in

main.py
    - class
    - called by a UI script
    - gets cycles from folder in domain / one in cycles tab
    - runs whatever processes
    - 
"""
import os
import logging
from generation import TurnedGenerate
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
            
            turn = position.get("turn", 0)
            point = position.get("point", 0)
            
            start_directory = os.path.join("saves", self.save, "start")
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