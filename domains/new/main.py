import logging
import src.commands as commands
from domains.new.turn_manager import Turns

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
        try:
            self.config = commands.load_json("domains/new/config.json")
            logging.info(f"Config loaded: {self.config}")

            self.details = commands.load_json("domains/new/details.json")
            logging.info(f"Details loaded: {self.details}")
        except Exception as e:
            logging.error(f"Error loading settings: {e}")

    def main(self):
        try:
            turn_manager = Turns(f"saves/{self.save}")
        except Exception as e:
            logging.error(f"Error during main execution: {e}")
            
        turn_manager.iterate()
        turn_manager.iterate()
        turn_manager.iterate()
        turn_manager.iterate()
        turn_manager.iterate()