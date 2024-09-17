"""
Basic commands for managing files used across the project

List(directory)
    return list of folders in given directory

Save_txt + save_json
    Save txt / json file W given name + contents

read_txt + load_json
    Get contents of given txt / json file
    
create_directory
    Make given directory

file_name includes the directories, everything works from the root directory
"""

import os
import json

def list(directory_path):
    folder_names = []
    if not os.path.exists(directory_path):
        print(f"Error: Domain directory does not exist.")
    try:
        items = os.listdir(directory_path)
        for item in items:
            item_path = os.path.join(directory_path, item)
            if os.path.isdir(item_path):
                folder_names.append(item)
                
    except OSError as e:
        print(f"Error: Unable to list contents of directory '{directory_path}'. ")    
        print(e)
    return folder_names
    
def save_txt(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error occurred while saving text file '{file_name}': {e}")

def read_txt(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return ''

def save_json(file_name, contents):
    try:
        with open(file_name, 'w') as f:
            json.dump(contents, f, indent=4)
    except (IOError, PermissionError) as e:
        print(f"Error saving to {file_name}: {e}")

def load_json(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_name}.")
        return None
    
def create_directory(directory):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            print(f"Error creating directory '{directory}': {e}")