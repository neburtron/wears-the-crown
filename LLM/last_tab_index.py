import os
import src.utils as utils

import logging
logging.basicConfig(level=logging.INFO)

def get_last_tab_index(folder):
    index_file = os.path.join(folder, "last_tab_index.txt")
    if os.path.exists(index_file):
        with open(index_file, 'r') as file:
            index = int(file.read().strip())
            return index
    return 0

def save_last_tab_index(folder, index):
    index_file = os.path.join(folder, "last_tab_index.txt")
    with open(index_file, 'w') as file:
        file.write(str(index))
        
def save_settings(self, entry_vars, settings_file):
    settings_data = {setting: entry_var.get() for setting, entry_var in entry_vars.items()}
    try:
        utils.save_json(settings_file, settings_data)
        logging.info(f"Settings saved to {settings_file}")
    except Exception as e:
        logging.error(f"Failed to save settings: {e}")