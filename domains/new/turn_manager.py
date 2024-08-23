import os
import shutil
import src.commands as commands
from domains.new.event_manager import EventManager

class Turns:

    def __init__(self, save):
        self.save = save
        self.turn_dir = os.path.join(save, "Turns")
        commands.create_directory(self.turn_dir)
        self.things_repeat = []
        self.things_single = []        
        self.subdirs = ["repeated", "single"]
        
        current_dir = os.path.join(save, "start", "current")
        for subdir in self.subdirs:
            commands.create_directory(os.path.join(current_dir, subdir))

        # Initialize both repeated and single events
        self.get_existing(self.subdirs[0])
        self.get_existing(self.subdirs[1])

    def get_existing(self, subdir):
        if not isinstance(subdir, str):
            raise ValueError(f"Expected subdir to be a string, got {type(subdir).__name__}")
        
        files = []
        events = []
        path = os.path.join(self.save, "start", "current", subdir)
        subdir_files = commands.list(path)
        files.extend([os.path.join(path, file) for file in subdir_files])
        
        for file in files:
            try:
                contents = commands.load_json(file)
                until = contents.get('until', 0)
                period = contents.get('period', None)
            
                if period is not None:
                    events.append({'until': until, 'period': period, 'file_name': file})
                else:
                    events.append({'until': until, 'file_name': file})
            except Exception as e:
                print(f"Error loading file {file}: {e}")
        return events

    def add_repeat(self, until, period, file_name):
        self.things_repeat.append({'until': until, 'period': period, 'file_name': file_name})
        
    def add_single(self, until, file_name):
        self.things_single.append({'until': until, 'file_name': file_name})   

    def iterate(self):
        self.things = []
        
        # Initialize both repeated and single events
        self.get_existing(self.subdirs[0])
        self.get_existing(self.subdirs[1])
        
        # Process repeated tasks
        for item in self.things_repeat:
            self.run(item)
            
        # Process single tasks
        self.things_single = [self.run(item) for item in self.things_single if item['until'] > 0]
        self.move_files()
        EventManager(self.things)
        
    def run(self, item):
        item['until'] -= 1
        
        # If the task is ready to be executed, add it to `self.things`
        if item['until'] < 1:
            self.things.append(item)            
            # Reset the period for repeated tasks
            if 'period' in item:
                item['until'] = item['period']
        return item
    
    def move_files(self):
        turn_number = self.get_next_turn_number()
        turn_path = os.path.join(self.turn_dir, f"turn_{turn_number}")
        commands.create_directory(turn_path)

        for item in self.things_repeat + self.things_single:
            src_file = item['file_name']
            dst_file = os.path.join(turn_path, os.path.basename(src_file))
            try:
                shutil.move(src_file, dst_file)
                print(f"Moved file {src_file} to {dst_file}")
            except Exception as e:
                print(f"Error moving file {src_file}: {e}")

    def get_next_turn_number(self):
        existing_turns = commands.list(self.turn_dir)
        if existing_turns:
            numbers = [int(turn.split('_')[1]) for turn in existing_turns if turn.startswith("turn_")]
            next_number = max(numbers, default=0) + 1
        else:
            next_number = 1
        return next_number