import src.utils as utils
import core.conversation as conversation
from scripts.data_storage import Info
import os
class Run:
    def __init__(self, save):
        self.save = os.path.join("saves", save)
        self.config = utils.load_json(f"{self.save}/start/config.json")
        self.turn = self.config.get("turn", 0)  # Default to turn 1 if "turn" is not found

        self.characters = Info(self.save)
        
        self.start_turn()
    
    def get_char_data(self, folder=None):
        if folder is None:
            self.characters.get_data("DEFAULT_FOLDER", self.turn - 1)  # Replace with appropriate folder
        else:
            self.characters.get_data(folder)
        
        return self.characters.retrieve_data()
    
    def retrieve_char_data(self, folder=None):
        if self.characters is not None:
            return self.characters.retrieve_data()
        else:
            return self.get_char_data(folder)
    
    
    def start_turn(self):
        characters_folder = os.path.join(self.save, "now", "characters")
        character_info = self.retrieve_char_data()
        
    
    def re1trieve_char_data(self, folder=None):
        # Combine the logic with get_char_data for simplicity
        return self.get_char_data(folder)
    
    def sta1rt_turn(self):
        characters_folder = os.path.join(self.save, "now", "characters")
        character_info = self.retrieve_char_data()

        if character_info is None:
            print("No character info found. Initializing default characters.")
            # Add any fallback logic or initialization here.
