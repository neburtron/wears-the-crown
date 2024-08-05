import tkinter as tk					 
from tkinter import ttk 
import os
import src.settings_manager as settings

class LLMSettingsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LLM Settings")
        self.root.minsize(height=500, width=500)
        self.root.geometry("500x500")
        
        self.settings_files = {
            'OpenAI':      os.path.join(settings.SETTINGS_FOLDER, "OpenAI.json"),
            'HuggingFace': os.path.join(settings.SETTINGS_FOLDER, "HuggingFace.json")
        }
        self.init_gui()
        
    def init_gui(self):
        self.label = ttk.Label(self.root, text="Edit LLM Settings\n\nSelect the tab of the API you want to use.")
        self.label.pack(pady=10)
        
        self.tabControl = ttk.Notebook(self.root)
        self.tabControl.bind("<<NotebookTabChanged>>", self.on_tab_changed)
        
        self.frames = {}
        for name in ['OpenAI', 'HuggingFace']:
            frame = ttk.Frame(self.tabControl)
            self.tabControl.add(frame, text=name)
            self.frames[name] = frame
            
            settings_data = settings.get_settings(name.lower())
            self.create_settings_widgets(frame, settings_data, self.settings_files[name])
        
        last_tab_index = settings.get_last_tab_index()
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
        settings.save_settings(settings_file, settings_data)
    
    def on_tab_changed(self, event):
        selected_tab_index = self.tabControl.index("current")
        settings.save_last_tab_index(selected_tab_index)

def run_llm_settings():
    root = tk.Tk()
    app = LLMSettingsApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_llm_settings()