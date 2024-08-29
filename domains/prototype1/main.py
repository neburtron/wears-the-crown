import src.utils as utils
import game_stuff.conversation as conversation
import os
import json


class Run:
    
    def __init__(self, save):
        self.save = os.path.join("saves", save)
        config = utils.load_json("domains/prototype1/config.json")
        details = utils.load_json("domains/prototype1/details.json")
        
        self.turn = config.get("turn", None)  # Ensure a default value if "turn" is not found
        self.start_turn()
    
    def get_data(self, character_folder):
        stored_info = []
        characters = utils.list(character_folder)
        
        for character in characters:
            try:
                char_data = utils.load_json(f"{character_folder}/{character}")
                stored_info.append(char_data)
            except FileNotFoundError:
                print(f"Error: Character file {character} not found.")
            except json.JSONDecodeError:
                print(f"Error: Could not decode JSON for character {character}.")
            
        return stored_info
    
    def start_turn(self):
        characters_folder = os.path.join(self.save, "now", "characters")
        
        character_info = self.get_data(characters_folder)
        
                
        pass
