import os
import shutil
import src.commands as commands

SETTINGS_FOLDER = "settings"
TEMPLATES_FOLDER = os.path.join(SETTINGS_FOLDER, "templates")
LTI = "last_tab_index.txt"

def get_settings(service_name):
    settings_file = os.path.join(SETTINGS_FOLDER, f"{service_name}.json")
    if not os.path.exists(settings_file):
        template_file = os.path.join(TEMPLATES_FOLDER, f"{service_name}Template.json")
        if os.path.exists(template_file):
            shutil.copyfile(template_file, settings_file)
        else:
            raise FileNotFoundError(f"Template file '{template_file}' does not exist.")
    return commands.load_json(settings_file)

def save_settings(service_name, settings_data):
    settings_file = os.path.join(SETTINGS_FOLDER, f"{service_name}.json")
    commands.save_json(settings_file, settings_data)

def get_last_tab_index():
    index_file = os.path.join(SETTINGS_FOLDER, LTI)
    if os.path.exists(index_file):
        with open(index_file, "r") as file:
            return int(file.read().strip())
    return 0

def save_last_tab_index(index):
    index_file = os.path.join(SETTINGS_FOLDER, LTI)
    with open(index_file, "w") as file:
        file.write(str(index))
        
