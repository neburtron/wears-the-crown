import os

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