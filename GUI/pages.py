import tkinter as tk
from tkinter import ttk
import os
import shutil
import src.commands as commands

import logging
logging.basicConfig(level=logging.INFO)


class Page(tk.Frame):
    def __init__(self, parent, manager, create_save_callback, return_save_callback):
        super().__init__(parent)
        self.manager = manager
        self.create_save_callback = create_save_callback
        self.return_save_callback = return_save_callback
        self.pack(fill="both", expand=True)

    def create_button(self, text, command, **pack_options):
        button = tk.Button(self, text=text, command=command)
        button.pack(pady=5, **pack_options)
        return button
    
    def create_label(self, text, **pack_options):
        label = tk.Label(self, text=text)
        label.pack(pady=5, **pack_options)
        return label

    def create_listbox(self, items, select_command, **pack_options):
        listbox = tk.Listbox(self)
        for item in items:
            listbox.insert(tk.END, item)
        listbox.pack(pady=5, **pack_options)
        listbox.bind('<<ListboxSelect>>', select_command)
        return listbox


class StartPage(Page):
    def __init__(self, parent, manager, create_save_callback=None, start_game_callback=None, return_save_callback=None):
        super().__init__(parent, manager, create_save_callback, start_game_callback)
        self.create_label("Main Menu")
        self.create_buttons()

    def create_buttons(self):
        self.create_button("LLM Settings", lambda: self.manager.show_frame("LLMSettingsPage"))
        self.create_button("Play", lambda: self.manager.show_frame("SaveSelectionPage"))


class LLMSettingsPage(Page):
    def __init__(self, parent, manager, create_save_callback=None, return_save_callback=None):
        super().__init__(parent, manager, create_save_callback, return_save_callback)

        self.create_label("LLM Settings")
        
        self.folder = "settings"
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)
        
        self.create_openai_tab()
        self.create_huggingface_tab()
        
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)
        
        self.create_button("Back", self.on_back)
        
        last_tab_index = self.get_last_tab_index()
        self.notebook.select(last_tab_index)
        
    def create_openai_tab(self):
        openai_frame = ttk.Frame(self.notebook)
        self.notebook.add(openai_frame, text="OpenAI")
        
        settings_file = os.path.join(self.folder, "openai.json")
        settings = commands.load_json(settings_file)
        self.create_settings_widgets(openai_frame, settings, settings_file)

    def create_huggingface_tab(self):
        huggingface_frame = ttk.Frame(self.notebook)
        self.notebook.add(huggingface_frame, text="HuggingFace")
                
        settings_file = os.path.join(self.folder, "huggingface.json")
        settings = commands.load_json(settings_file)
        self.create_settings_widgets(huggingface_frame, settings, settings_file)
        

    def on_tab_changed(self, event):
        selected_tab_index = self.notebook.index("current")
        self.save_last_tab_index(selected_tab_index)
        
    
    def get_settings(self, name):
        settings_file = os.path.join(self.folder, f"{name}.json")
        if not os.path.exists(settings_file):
            template_file = os.path.join(self.folder, "templates", f"{name}.json")
            os.makedirs(os.path.dirname(settings_file), exist_ok=True)
            shutil.copyfile(template_file, settings_file)
        return commands.load_json(settings_file)

    def save_last_tab_index(self, index):
        index_file = os.path.join(self.folder, "last_tab_index.txt")
        with open(index_file, "w") as file:
            file.write(str(index))
            
    def create_settings_widgets(self, frame, model_settings, settings_file):
        entry_vars = {}
        for setting, value in model_settings.items():
            label = ttk.Label(frame, text=setting)
            label.pack(pady=5, anchor="w", padx=5)
            
            entry_var = tk.StringVar(value=value)
            entry_vars[setting] = entry_var
            
            entry = ttk.Entry(frame, textvariable=entry_var)
            entry.pack(pady=5, anchor="w", padx=5)
            
        save_button = ttk.Button(frame, text="Save", command=lambda: self.save_settings(entry_vars, settings_file))
        save_button.pack(pady=10)

    def save_settings(self, entry_vars, settings_file):
        settings_data = {setting: entry_var.get() for setting, entry_var in entry_vars.items()}
        try:
            commands.save_json(settings_file, settings_data)
            logging.info(f"Settings saved to {settings_file}")
        except Exception as e:
            logging.error(f"Failed to save settings: {e}")
            
    def get_last_tab_index(self):
        index_file = os.path.join(self.folder, "last_tab_index.txt")
        if os.path.exists(index_file):
            with open(index_file, "r") as file:
                index = int(file.read().strip())
                if index < self.notebook.index("end"):
                    return index
        return 0
    
    def on_back(self):
        self.manager.show_frame("StartPage")
        
class SaveSelectionPage(Page):
    def __init__(self, parent, manager, create_save_callback, return_save_callback=None):
        super().__init__(parent, manager, create_save_callback, return_save_callback)
        self.create_label("Existing Saves")
        saves = self.get_saves()
        self.listbox = self.create_listbox(saves, self.on_select)
        
        self.entry_label = self.create_label("Enter save name:")
        self.save_name_entry = tk.Entry(self)
        self.save_name_entry.pack(pady=5)

        self.create_button("Submit", self.on_submit)
        self.create_button("Back", self.on_back)

    def get_saves(self):
        try:
            return os.listdir("saves")
        except FileNotFoundError:
            print("Saves directory not found.")
            return []
    def return_save(self, save):
        self.return_save_callback(save)
        
    def on_submit(self):
        save_name = self.save_name_entry.get().strip()
        if not save_name:
            print("Save name cannot be empty.")
            return

        if any(char in save_name for char in r'\/:*?"<>|'):
            print("Save name contains invalid characters.")
            return

        self.return_save(save_name)
        self.manager.show_frame("DomainSelectionPage")

    def on_back(self):
        self.manager.show_frame("StartPage")

    def on_select(self, event):
        selected_idx = self.listbox.curselection()
        
        if selected_idx:
            save_name = self.listbox.get(selected_idx[0])
            self.return_save(save_name)
            self.manager.show_frame("DomainSelectionPage")

class DomainSelectionPage(Page):
    def __init__(self, parent, manager, create_save_callback, return_save_callback=None):
        super().__init__(parent, manager, create_save_callback, return_save_callback)
        self.create_label("Select Domain")
        self.listbox = self.create_listbox([], self.on_select)
        self.create_button("Back", self.on_back)
        self.update_domains()
        
    def update_domains(self):
        domains = commands.list("domains")
        self.listbox.delete(0, tk.END)
        for domain in domains:
            self.listbox.insert(tk.END, domain)

    def on_select(self, event):
        selected_idx = self.listbox.curselection()
        if selected_idx:
            selected_domain = self.listbox.get(selected_idx[0])
            self.create_save_callback(selected_domain)

    
    def on_back(self):
        self.manager.show_frame("StartPage")