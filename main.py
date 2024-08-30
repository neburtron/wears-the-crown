from gui.main_gui import GuiManager
from gui.save_creation_gui import StartGui
class Main:
    def __init__(self):
        self.save_name = None
        self.gui_manager = GuiManager()
        self.start_gui = StartGui(self.gui_manager)  # Pass GuiManager to StartGui
        self.gui_manager.start()

if __name__ == "__main__":
    Main()