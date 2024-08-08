import tkinter as tk
from tkinter import ttk
import GUI.pages as pages
        
class FrameManager:
    def __init__(self, root, title):
        self.root = root
        self.frames = {}
        self.root.title(title)
        self.root.minsize(height=500, width=500)
        self.root.geometry("500x500")
        self.create_save_callback = None
        self.return_save_callback = None
        self.init_gui()
        
    def init_gui(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
    def add_frame(self, frame_name, frame_class):
        frame = frame_class(self.root, self, self.create_save_callback, self.return_save_callback)
        frame.pack(fill="both", expand=True)
        self.frames[frame_name] = frame
        frame.pack_forget()
        print(f"Added frame: {frame_name}")

    def show_frame(self, frame_name):
        frame = self.frames.get(frame_name)
        if frame:
            for frm in self.frames.values():
                frm.pack_forget()
            frame.pack(fill="both", expand=True)
            frame.tkraise()
        else:
            print(f"Frame {frame_name} not found")

    def setup_frames(self, create_save_callback, return_save_callback):
        self.create_save_callback = create_save_callback
        self.return_save_callback = return_save_callback
        self.add_frame("StartPage", pages.StartPage)
        self.add_frame("LLMSettingsPage", pages.LLMSettingsPage)
        self.add_frame("DomainSelectionPage", pages.DomainSelectionPage)
        self.add_frame("SaveSelectionPage", pages.SaveSelectionPage)