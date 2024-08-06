import src.settings_manager as settings
from src.commands import SaveManager
import src.commands as commands
import src.terminal_stuff as terminal
from domains.testing.main import run as testing


def main():
    print("\n\nWelcome!\n\n")
    llm_query()
    domain_menu()

def llm_query():
    try:
        choose = terminal.choice(["y", "n"], "Do you want to change LLM settings? (Write Y for yes, N for no)", None, False)
        if choose == "y":
            tabs = {"OpenAI": "OpenAI", "HuggingFace": "HuggingFace"}
            settings.run_llm_settings(tabs, "settings")
    except Exception as e:
        print(f"Error in llm_query: {e}")

def domain_menu():
    domains = commands.list("domains")
    domain_selection = terminal.list_choices(domains, None, "Domains: ", "Select one from above.", False)
    
    if domain_selection == testing:
        instance = testing(saves_menu())  # Assuming the core module has a run function
    
def saves_menu():
    try:
        save_manager = SaveManager()
        saves = save_manager.list()
        save = terminal.choice(saves, "Available Saves:", "Enter the name of the save to load or create", False)
        if save in saves:
            print(f"Loading save: {save}")
            return(save)
        else:
            print(f"Creating new save: {save}")
            result = save_manager.create(save)
            if result == "Success":
                return(save)
            else:
                print(f"Failed to create save: {result}")
    except Exception as e:
        print(f"Error in saves_menu: {e}")

if __name__ == "__main__":
    main()