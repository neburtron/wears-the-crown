import os
import json
import shutil
class SaveManager:
    def create(self, save_name):
        try:
            save_path = f"saves/{save_name}"
            os.makedirs(save_path)
        
            # Define the template path and the initial turn directory
            template_path = "saves/startTemplate"
            initial_turn_path = os.path.join(save_path, "start")
        
            # Copy the template contents to the initial turn directory
            if os.path.exists(template_path):
                shutil.copytree(template_path, initial_turn_path)
            else:
                print(f"Template path '{template_path}' does not exist.")
                return "Template Not Found"
        
            print("\nSave Creation Success!\n")
            return "Success"
        except Exception as e:
            print(f"\nSave Creation Failed: {e}\n")
            return "Save Creation Failed"
        
    def list(self):
        folder_names = []
        directory_path = "saves"
        
        if not os.path.exists(directory_path):
            print(f"Error: Directory '{directory_path}' does not exist.")
            return folder_names
        
        try:
            items = os.listdir(directory_path)
            
            for item in items:
                item_path = os.path.join(directory_path, item)

                if os.path.isdir(item_path):
                    folder_names.append(item)
            
        except OSError as e:
            print(f"Error: Unable to list contents of directory '{directory_path}'.")
            print(e)
            
        return folder_names
    

def save_txt(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"Content successfully written to {file_name}")
    except Exception as e:
        print(f"Error occurred: {e}")

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return ''

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
    
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)