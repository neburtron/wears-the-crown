import json
import os


def save_json(filename, contents):
    try:
        with open(filename, 'w') as f:
            json.dump(contents, f, indent=4)
    except (IOError, PermissionError) as e:
        print(f"Error saving to {filename}: {e}")

def load_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filename}.")
        return None

def list_saves():
    folder_names = []
    directory_path = "saves"
    
    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        return folder_names
    
    try:
        # Get a list of all items (files and directories) in the specified directory
        items = os.listdir(directory_path)
        
        # Iterate over each item
        for item in items:
            item_path = os.path.join(directory_path, item)

            # Check if the item is a directory
            if os.path.isdir(item_path):
                folder_names.append(item)  # Add the directory name to the list
    
    except OSError as e:
        print(f"Error: Unable to list contents of directory '{directory_path}'.")
        print(e)
    
    return folder_names


def make_save(save):
    try:
        os.mkdir("Saves/" + save)
        print("\nSave Creation Success!\n")
        return "Success"
    except Exception as e:
       print(f"\nSave Creation Failed: {e}\n")
       return "Save Creation Failed"