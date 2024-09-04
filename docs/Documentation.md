# Core structure of project

The goal of this project is to be a modular framework that can be used to make games that utilize LLMs for a type of game that doesn't really exist right now. There are several modules that I seperated funcitonality into.

Actual functionality of this project is broken up into domains and scripts. Scripts are modular functionality that can be used across domains, domains are games made with the framework. They handle how scripts from both the scripts folder and ones that only work for that domain are called + the starting data and how that's interpreted.

The goal of this project is combining LLMs and structure to make magic. Individual scripts are rather simple, domains should be the creative application of that simpler functionality.

## Modules

NOTE - I don't know what I'm doing and will figure out better file organization as I go.

### 1. SRC

Basic commands that the whole project uses.

Utils.py is currently the only script here, and it handles basic file management stuff.

### 2. LLM

The LLM module handles direct LLM interactions.

LLM_Interface gets the selected LLM API, runs the corisponding script, and acts as the middleman for the rest of the project.

HuggingFace_Client.py is a placeholder, I haven't gotten around to dealing with that API / fully utilizing OpenAI's.

last_tab_index.py is used by the LLM settings screen in GUI/Pages, besides requiring one specific API to run your domain, I see no reason you'd need to worry about calling this script.

### 3. core

core stores general scripts that should be rather universal.

Currently I've put one script there, conversation.py; a WIP script that handles basic chatbot functionaility + stores chatlogs + handles chat responses.

### 4. scripts

Scripts is for less universal funcitonality, that should still be modular + isn't nessisarally only useful for one domain.

data_storage.py
contains info class

Info class is a generic class in charge of handling simple lists, arrays, whatever, and stuff like that.

### 5. GUI

Basic GUI for main menu. It's shit. Uses Tkinter, and handles settings, making saves, selecting saves, and domains. I don't have anything for the game itself, I'm gonna likely keep the terminal tests going for a little bit.

Somewhat modular, has a set of pages that you can swap between, and it includes old tabbed settings management script functionality I added before the main menu GUI.
