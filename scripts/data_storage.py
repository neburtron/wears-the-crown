"""
This script manages lists of items and their changes in a generalized manner.

Class Info:
- Handles saving, loading, and storing data of a certain type, associated with a given save name.
- Supports turn-based data management (optional).
- Allows for dynamic updating and saving of data to structured directories.

Attributes:
- name: The save name provided during initialization.
- savedir: The directory where the save data is stored (under "saves/name").
- location: The specific subdirectory or file location for saving/loading data.
- turn: The current turn, if applicable (can be None if not used).
- data: The data currently being managed by the script.

Methods:
- save_location(location, turn=None): Sets the desired save location. Optionally, updates the turn.
- get_data(location=None, turn=None): Loads data from the specified or default location/turn and returns it.
- retrieve_data(): Returns the currently loaded data.
- set_data(data, turns=0): Replaces the current data with the provided data. Optionally, adjusts the turn.
- save_data(location=None, turn=None, name=None): Saves the current data to the specified or default location, with the option to specify a filename.
- update_list(key, value): Adds a value to a list within the data, creating the list if it doesn't exist.
- remove_from_list(key, value): Removes a value from a list within the data.
"""

import src.utils as utils
import os


class Info:
    def __init__(self, name):
        self.name = name
        self.savedir = os.path.join("saves", self.name)
        self.location = None
        self.data = None
        self.turn = None

    def save_location(self, location, turn=None):
        self.location = location
        if turn is not None:
            self.turn = turn

    def get_data(self, location=None, turn=None):
        if location is None:
            location = self.location
        if turn is None:
            turn = self.turn
        
        directory = os.path.join(self.savedir, str(turn), location) if turn else os.path.join(self.savedir, location)
        self.data = utils.load_json(directory)
        return self.data

    def retrieve_data(self):
        return self.data

    def set_data(self, data, turns=0):
        self.data = data
        self.turn = self.turn + turns if self.turn is not None else turns

    def save_data(self, location=None, turn=None, name=None):
        if location is None:
            location = self.location
        if turn is None:
            turn = self.turn
        if name is None:
            name = location
        
        directory = os.path.join(self.savedir, str(turn), location, f"{name}.json") if turn else os.path.join(self.savedir, location, f"{name}.json")
        utils.save_json(directory, self.data)
            utils.save_json(location, self.data)

    def update_list(self, key, value):
        """
        Generalized method to update lists within the data.
        Appends the value to the list identified by 'key'. 
        Creates a new list if the key doesn't exist.
        """
        if self.data is None:
            raise ValueError("Data is not loaded. Please use get_data() first.")
        
        if key not in self.data:
            self.data[key] = []
        
        self.data[key].append(value)

    def remove_from_list(self, key, value):
        """
        Generalized method to remove a value from a list within the data.
        """
        if self.data is None:
            raise ValueError("Data is not loaded. Please use get_data() first.")
        
        if key in self.data and value in self.data[key]:
            self.data[key].remove(value)