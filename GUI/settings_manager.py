import tkinter as tk					 
from tkinter import ttk 
import os
import shutil
import src.commands as commands

class settings_app:
    def __init__(self, root, title, tabs, header, text1, folder):
        self.tabs = tabs
        self.folder = folder
        self.template_folder = os.path.join(folder, "templates")
        self.backend = settings_manager(folder)
        
        self.root = root
        self.root.title(title)
        self.root.minsize(height=500, width=500)
        self.root.geometry("500x500")
        
        self.init_gui(header, text1)
        
    def init_gui(self, header, text1):
        self.label = ttk.Label(self.root, text=f"{header}\n\n{text1}")
        self.label.pack(pady=10)
        
        self.tabControl = ttk.Notebook(self.root)
        self.tabControl.bind("<<NotebookTabChanged>>", self.on_tab_changed)
        
        self.frames = {}
        for name in self.tabs:
            frame = ttk.Frame(self.tabControl)
            self.tabControl.add(frame, text=name)
            self.frames[name] = frame
            
            settings_data = self.backend.get_settings(name.lower())
            
            self.create_settings_widgets(frame, settings_data, self.tabs[name])
        
        last_tab_index = self.backend.get_last_tab_index()
        self.tabControl.select(last_tab_index)
        
        self.tabControl.pack(expand=1, fill="both")

    def create_settings_widgets(self, frame, model_settings, settings_file):
        row = 1
        entry_vars = {}
        for setting, value in model_settings.items():
            ttk.Label(frame, text=setting).grid(column=0, row=row, padx=5, pady=5)
            entry_var = tk.StringVar(value=value)
            entry_vars[setting] = entry_var
            ttk.Entry(frame, textvariable=entry_var).grid(column=1, row=row, padx=5, pady=5)
            row += 1

        save_button = ttk.Button(frame, text="Save", command=lambda: self.save_settings(entry_vars, settings_file))
        save_button.grid(column=0, row=row, columnspan=2, pady=10)

    def save_settings(self, entry_vars, settings_file):
        settings_data = {setting: entry_var.get() for setting, entry_var in entry_vars.items()}
        self.backend.save_settings(settings_file, settings_data)

    def on_tab_changed(self, event):
        selected_tab_index = self.tabControl.index("current")
        self.backend.save_last_tab_index(selected_tab_index)

def run_llm_settings(tabs, folder):
    root = tk.Tk()
    title = "LLM Settings"
    header = "LLM Settings Configuration"
    text1 = "Configure your LLM settings here."
    app = settings_app(root, title, tabs, header, text1, folder)
    root.mainloop()

class settings_manager():
    def __init__(self, folder):
        self.folder = folder
    
    def get_settings(self, name):
        settings_file = os.path.join(self.folder, f"{name}.json")
        if not os.path.exists(settings_file):
            template_file = os.path.join(self.folder, "templates", f"{name}.json")
            if os.path.exists(template_file):
                shutil.copyfile(template_file, settings_file)
            else:
                raise FileNotFoundError(f"Template file '{template_file}' does not exist.")
        return commands.load_json(settings_file)
    
    def save_settings(self, service_name, settings_data):
        settings_file = os.path.join(self.folder, f"{service_name}.json")
        try:
            commands.save_json(settings_file, settings_data)
        except Exception as e:
            print(f"Failed to save settings: {e}")

    def get_last_tab_index(self):
        index_file = os.path.join(self.folder, "last_tab_index.txt")
        if os.path.exists(index_file):
            with open(index_file, "r") as file:
                return int(file.read().strip())
        return 0

    def save_last_tab_index(self, index):
        index_file = os.path.join(self.folder, "last_tab_index.txt")
        with open(index_file, "w") as file:
            file.write(str(index))
            
            

if __name__ == "__main__":
    tabs = {"OpenAI": "OpenAI Settings", "HuggingFace": "Hugging Face Settings"}
    run_llm_settings(tabs, "./settings")