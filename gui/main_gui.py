import dearpygui.dearpygui as dpg
from gui.llm_gui import *

class GuiManager:
    def __init__(self, title="The Head that Wears the Crown", width=800, height=600):
        dpg.create_context()
        dpg.create_viewport(title=title, width=width, height=height)
        dpg.setup_dearpygui()

    def start(self):
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def add_window(self, window_name, content_func, tag=None):
        if tag:
            with dpg.window(label=window_name, tag=tag):
                content_func()
        else:
            with dpg.window(label=window_name):
                content_func()