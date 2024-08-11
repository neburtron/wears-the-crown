"""
script for basic agent functionality

in init:
gets info about agent from provided json
gets what save + region the agent is in 
gets current turn

New Turn Function
LLM given result of last turn + directories update
run plan + act functions

Plan function:
take old goals + evaluate / consider W new info
update plans W new info + last summarized info
run unwritten summarize script's ammend function to deal with new happenings


Act Function:
LLM given things it can do + it decides what it wants to do
based on info it's got access to
sends that out

yeah
 
"""

import src.commands as commands

class Agent:
    
    def __init__(self, info, save, turn, position):
        self.info = commands.load_json(info)
        self.save = save
        self.turn = turn
        self.position = position
        
    def new_turn(self):
        return
    
    def plan(self):
        return
    
    def act(self):
        return