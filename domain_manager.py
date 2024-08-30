import os
import shutil
import importlib
import src.utils as utils

class DomainManager:
    def __init__(self, save_directory="saves"):
        self.save_directory = save_directory
    
    def load_domain(self, save_name):
        path = os.path.join(self.save_directory, save_name, "start", "details.json")
        settings = utils.load_json(path)
        domain = settings.get("domain")
        return domain
    
    def create_save(self, save_name, domain):
        save_path = os.path.join(self.save_directory, save_name)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
            template_path = f"domains/{domain}/starting_data/StartTemplate"
            if os.path.exists(template_path):
                shutil.copytree(template_path, os.path.join(save_path, "start"))
            else:
                print(f"Template path '{template_path}' does not exist.")
        else:
            print(f"Path '{save_path}' already exists.")
        
    def run_domain(self, save_name):
        domain = self.load_domain(save_name)
        try:
            module = importlib.import_module(f"domains.{domain}.main")
            domain_function = getattr(module, "Run")
            domain_function(save_name)
        except Exception as e:
            print(f"Error running Domain: {e}")