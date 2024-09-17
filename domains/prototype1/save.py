import os
import shutil

import src.utils as utils

template_path = "LATER"
domain = "domains/prototype1"

def make_save(save_path):
    template_path = f"domains/{domain}/starting_data/StartTemplate"
    if os.path.exists(template_path):
            shutil.copytree(template_path, os.path.join(save_path, "start"))
    else:
        print(f"Template path '{template_path}' does not exist.")
        
def load_save(save_path):
    return
