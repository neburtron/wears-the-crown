import os
import shutil
import importlib
import tkinter as tk

from GUI.main_window import FrameManager
import src.commands as commands

class Main:
    def __init__(self):
        self.changed_settings = False
        self.domain = None   
        self.save = None
        self.root = tk.Tk()
        
        self.manager = FrameManager(self.root, "The Head that Wears the Crown")
        self.manager.setup_frames(self.create_save, self.return_save)
        self.manager.show_frame("StartPage")
        self.root.mainloop()
        
    def return_save(self, save):
        # Callback to store save name when selected
        if save is not None:
            self.save = save
            if os.path.exists(os.path.join("saves", save)):
                self.update_domain_from_save(save)
            
    def update_domain_from_save(self, save):
        path = os.path.join("saves", save, "state.json")
        settings = commands.load_json(path)
        self.domain = settings.get("domain")
        self.run_domain(os.path.dirname(path), self.domain)
            
    def create_save(self, domain):
        self.save = self.save or "default_save_name"  # Ensure self.save is initialized
        self.run_domain(os.path.join("saves", self.save), domain)
        
    def run_domain(self, path, domain):
        if not os.path.exists(path):
            os.makedirs(path)
            template_path = f"domains/{domain}/starting_data/StartTemplate"
            initial_turn_path = os.path.join(path, "start")
            if os.path.exists(template_path):
                shutil.copytree(template_path, initial_turn_path)
                commands.save_json(os.path.join(path, "state.json"), {"domain": domain, "turn": 0})
            else:
                print(f"Template path '{template_path}' does not exist.")
        try:
            module = importlib.import_module(f"domains.{domain}.main")
            domain_function = getattr(module, "run")
            domain_function(self.save)
        except Exception as e:
            print(f"Error running Domain: {e}")
        
if __name__ == "__main__":
    instance = Main()
    
    