import playground
from src.commands import SaveManager
import select_llm_details

def main():
    print("Welcome!\n\n")
    print("Do you want to change LLM settings? (write Y for yes, N for no)")
    choose = input().strip().upper()
    
    if choose == "Y":
        select_llm_details.run_llm_settings()
    elif choose != "N":
        print("Invalid input. Exiting...")
        return
    saves_menu()

def saves_menu():
    save_manager = SaveManager()
    saves = save_manager.list()
    
    if saves:
        print("Available saves:")
        for save in saves:
            print(f"- {save}")
    else:
        print("No saves available.")
    
    save = input("Enter the name of the save to load or create: ").strip().lower()
    
    if save in saves:
        print(f"Loading save: {save}")
        playground.main(save, "prompt") # save name, prompt file name
    else:
        print(f"Creating new save: {save}")
        result = save_manager.create(save)
        if result == "Success":
            playground.main(save, "prompt") # save name, prompt file name
        else:
            print(f"Failed to create save: {result}")

if __name__ == "__main__":
    main()