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
    
    def change_settings(self):
        return
    
    def return_save(self, save):
        # Callback to store save name when selected
        self.save = save
        print(f"Save returned: {self.save}")
        self.update_domain_from_save(save)

    def update_domain_from_save(self, save):
        # domain extraction logic here
        self.domain = "testing"  # Placeholder, adjust based on your logic
        print(f"Domain for the selected save '{save}' is '{self.domain}'")
    
    def create_save(self, save_name, domain, existing):
        """
        This function is run if the user tries to make a new save
        
        This is run after the user gives the domain they'd like to use
        
        The save itself is collected in the return_save function + set to self.save
        
        First the save dir is created
        Then the save files for the domain are taken and copied to the save path
        At the same time state.json is created - THIS IS TO BE REMOVED OR REDONE
        That's about it, minus error stuff.
        """
        try:
            save_path = f"saves/{self.save}"
            os.makedirs(save_path)
            
            template_path = f"domains/{domain}/starting_data/StartTemplate"
            initial_turn_path = os.path.join(save_path, "start")
            
            if os.path.exists(template_path):
                shutil.copytree(template_path, initial_turn_path)
                commands.save_json(f"{save_path}/state.json", [{"turn":0}, {"point":0}])
            else:
                print(f"Template path '{template_path}' does not exist.")
                return "Template Not Found"
            
            print("\nSave Creation Success!\n")
            self.run_domain(domain)
            return "Success"
        
        except Exception as e:
            print(f"\nSave Creation Failed: {e}\n")
            return "Failed"

    def run_domain(self, domain):
        try:
            module = importlib.import_module(f"domains.{domain}.main")
            domain_function = getattr(module, "run")
            domain_function(self.save)
        except Exception as e:
            print(f"Error running Domain: {e}")
            
if __name__ == "__main__":
    instance = Main()