import logging
logging.basicConfig(level=logging.INFO)

class ArrayManager:
    
    def __init__(self):
        self.array = []
        
    def input(self, person, message):
        self.array.append({person: message})
        
    def input_many(self, array):
        for person, message in array:
            self.input(f"role: {person}", f"content: {message}")

    def clear(self):
        self.array = []
        
    def print(self):
        for person, message in self.array:
            logging.info(f"\n {person}: {message}\n")
