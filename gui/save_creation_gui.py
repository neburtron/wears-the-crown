import dearpygui.dearpygui as dpg
from domain_manager import DomainManager
import src.utils as utils
from gui.llm_gui import *
from gui.llm_gui import LLMSettingsPage

class StartGui:
    def __init__(self, gui_manager):
        self.gui_manager = gui_manager
        self.setup_main_window()

    def setup_main_window(self):
        self.gui_manager.add_window("Main Menu", self.main_menu)

    def main_menu(self):
        dpg.add_text("MAIN MENU")
        dpg.add_button(label="Start", callback=self.new_game)
        dpg.add_button(label="Saves List", callback=self.open_saves)
        dpg.add_button(label="LLM Settings", callback=self.llm_settings)

    def new_game(self):
        NewGameGui(self.gui_manager)

    def open_saves(self):
        SavesGui(self.gui_manager)

    def llm_settings(self):
        LLMSettingsPage(self.gui_manager, self.gui_manager)
        
class NewGameGui:
    def __init__(self, gui_manager):
        self.gui_manager = gui_manager
        self.saves = utils.list("saves")
        self.name = ""
        self.create_window()

    def create_window(self):
        self.gui_manager.add_window("New Game", self.setup_new_game, tag="new_game_window")

    def setup_new_game(self):
        with dpg.group():
            self.name_window()
                
    def name_window(self):
        dpg.add_input_text(
            label="Save Name", 
            tag="save_name_input",
            callback=self.handle_input,
            on_enter=True
        )

    def handle_input(self, sender, app_data, user_data):
        if app_data is not None:
            self.name = app_data
            if self.name in self.saves:
                details = utils.load_json(f"saves/{self.name}/start/details.json")
                domain = details.get("domain")
                InfoGui(self.gui_manager, self.name, domain, False)
            else:
                DomainGui(self.gui_manager, self.name)

class SavesGui:
    def __init__(self, gui_manager):
        self.gui_manager = gui_manager
        self.create_window()

    def create_window(self):
        self.gui_manager.add_window("Saves List", self.saves_window)

    def saves_window(self):
        saves = utils.list("saves")
        dpg.add_listbox(items=saves, enabled=False)
        
class DomainGui:
    def __init__(self, gui_manager, name):
        self.name = name
        self.gui_manager = gui_manager
        self.create_window()

    def create_window(self):
        self.gui_manager.add_window("Select Domain", self.domains_window)

    def domains_window(self):
        domains = utils.list("domains")
        dpg.add_listbox(items=domains, callback=self.display_stats, tag="domains_listbox")

    def display_stats(self, sender, app_data):
        InfoGui(self.gui_manager, self.name, app_data, True)
        
class InfoGui:
    def __init__(self, gui_manager, name, domain, new):
        self.gui_manager = gui_manager
        self.name = name
        self.domain = domain
        self.new = new
        self.create_window()

    def create_window(self):
        self.gui_manager.add_window("Info", self.display_window)
        self.domain_manager = DomainManager()

    def display_window(self):
        dpg.add_text("Info about Save:")
        dpg.add_text(f"Name: {self.name}")
        dpg.add_text(f"Domain: {self.domain}")
        
        dpg.add_button(label="confirm", callback=self.confirm)
        
    def confirm(self):
        if self.new:
            self.create_save()
        else:
            self.load_save()
            
    def create_save(self):
        if not self.name:
            self.name = "default_save_name"
        self.domain_manager.create_save(self.name, self.domain)
        self.domain_manager.run_domain(self.name)

    def load_save(self):
        self.save_name = self.name
        self.domain_manager.run_domain(self.name)