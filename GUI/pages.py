import tkinter as tk
import os
import src.commands as commands

class Page(tk.Frame):
    def __init__(self, parent, manager, create_save_callback=None, start_game_callback=None, return_save_callback=None):
        super().__init__(parent)
        self.manager = manager
        self.create_save_callback = create_save_callback
        self.start_game_callback = start_game_callback
        self.return_save_callback = return_save_callback
        self.pack(fill="both", expand=True)

    def create_button(self, text, command):
        button = tk.Button(self, text=text, command=command)
        button.pack(pady=5)
        return button
    
    def create_label(self, text):
        label = tk.Label(self, text=text)
        label.pack(pady=5)
        return label

    def create_listbox(self, items, select_command):
        listbox = tk.Listbox(self)
        for item in items:
            listbox.insert(tk.END, item)
        listbox.pack(pady=5)
        listbox.bind('<<ListboxSelect>>', select_command)
        return listbox

class StartPage(Page):
    def __init__(self, parent, manager, create_save_callback=None, start_game_callback=None, return_save_callback=None):
        super().__init__(parent, manager, create_save_callback, start_game_callback, return_save_callback)
        self.create_label("Main Menu")
        self.create_buttons()

    def create_buttons(self):
        self.create_button("LLM Settings", lambda: self.manager.show_frame("LLMSettingsPage"))
        self.create_button("Play", lambda: self.manager.show_frame("SaveSelectionPage"))

class LLMSettingsPage(Page):
    def __init__(self, parent, manager, create_save_callback=None, start_game_callback=None, return_save_callback=None):
        super().__init__(parent, manager, create_save_callback, start_game_callback, return_save_callback)
        self.create_label("LLM Settings")
        self.create_button("Back", self.on_back)

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

    def on_submit(self):
        save_name = self.save_name_entry.get().strip()
        if save_name:
            if save_name in self.get_saves():
                self.create_save_callback(save_name, existing=True)
            else:
                self.manager.show_frame("DomainSelectionPage")

    def on_back(self):
        self.manager.show_frame("StartPage")

    def on_select(self, event):
        selected_idx = self.listbox.curselection()
        if selected_idx:
            save_name = self.listbox.get(selected_idx[0])
            self.manager.show_frame("DomainSelectionPage", save_name)

class DomainSelectionPage(Page):
    def __init__(self, save_name, parent, manager, create_save_callback, return_save_callback=None):
        super().__init__(parent, manager, create_save_callback, return_save_callback)
        self.save_name = save_name
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
            self.create_save_callback(save_name, selected_domain, existing=False)

    def on_back(self):
        self.manager.show_frame("StartPage")