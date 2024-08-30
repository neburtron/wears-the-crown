import dearpygui.dearpygui as dpg
import src.utils as utils
import llm.last_tab_index as last_tab
import os
import shutil

class LLMSettingsPage:
    def __init__(self, parent, manager):
        self.parent = parent
        self.manager = manager
        
        self.create_window()
        
        self.folder = "settings"
        last_tab_index = last_tab.get_last_tab_index(self.folder)
        dpg.set_value("notebook", last_tab_index)

    def create_window(self):
        with dpg.window(label="LLM Settings", tag="llm_settings_window"):
            with dpg.tab_bar(tag="notebook"):
                self.create_openai_tab()
                self.create_huggingface_tab()
                
                
    def create_openai_tab(self):
        with dpg.tab(label="OpenAI"):
            settings_file = os.path.join("settings", "openai.json")
            if not os.path.exists(settings_file):
                # Copy template from settings/templates
                template_file = os.path.join("settings", "templates", "OpenAI.json")
                shutil.copy(template_file, settings_file)
            settings = utils.load_json(settings_file)
            self.create_settings_widgets(settings, settings_file)

    def create_huggingface_tab(self):
        with dpg.tab(label="HuggingFace"):
            settings_file = os.path.join("settings", "HuggingFace.json")
            if not os.path.exists(settings_file):
                # Copy file from settings/templates
                template_file = os.path.join("settings", "templates", "HuggingFace.json")
                shutil.copy(template_file, settings_file)
            settings = utils.load_json(settings_file)
            self.create_settings_widgets(settings, settings_file)
   
    def create_settings_widgets(self, model_settings, settings_file):
        self.entry_vars = {}
        for setting, value in model_settings.items():
            dpg.add_text(setting, bullet=True)
            entry_var = dpg.add_input_text(default_value=value, tag=setting)
            self.entry_vars[setting] = entry_var
            
        dpg.add_button(label="Save", callback=lambda: self.save_settings(settings_file))

    def save_settings(self, settings_file):
        settings_data = {setting: dpg.get_value(entry_var) for setting, entry_var in self.entry_vars.items()}
        try:
            utils.save_json(settings_file, settings_data)
            print(f"Settings saved to {settings_file}")
        except Exception as e:
            print(f"Failed to save settings: {e}")
            