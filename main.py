"""
Main script in charge of initializing the main GUI script 
and adding the start menu to the GUI instance.

GUI handled by Dear PyGui

Other scripts in the gui module are windows that should be under the main_gui script.
"""

from gui.main_gui import GuiManager
from gui.save_creation_gui import StartGui


class Main:
    def __init__(self):
        self.save_name = None
        self.gui_manager = GuiManager()
        self.start_gui = StartGui(self.gui_manager)
        self.gui_manager.start()


if __name__ == "__main__":
    Main()