"""
This script acts as the middleman between GUI save creation and each domain's save.py script

Class DomainManager:
- Imports main.py and start.py scripts for given domain
- Imports and runs commands for given domain
- 

Attributes:
- name: The save name provided by user selection.
- save_directory: Overwrites default save directory used throught script.
   
Methods:
- load_domain(name):
- create_save(name, domain):
- run_domain(name):
"""

import os
import importlib
import src.utils as utils

class DomainManager:
    def __init__(self, save_directory="saves"):
        self.save_directory = save_directory
    
    def load_domain(self, name):
        path = os.path.join(self.save_directory, name, "start", "details.json")
        settings = utils.load_json(path)
        domain = settings.get("domain")
        return domain
    
    def create_save(self, name, domain):
        save = importlib.import_module(f"domains.{domain}.save.py")
        save_path = os.path.join(self.save_directory, name)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
            save.make_save(save_path)
        else:
            print(f"Path '{save_path}' already exists.")
        
    def run_domain(self, name, domain):
        try:
            module = importlib.import_module(f"domains.{domain}.main")
            domain_function = getattr(module, "Run")
            domain_function(name)
        except Exception as e:
            print(f"Error running Domain: {e}")