import os
import commands
import select_llm_details
import playground

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
    saves = commands.list_saves()
    
    if saves:
        print("Available saves:")
        for save in saves:
            print(f"- {save}")
    else:
        print("No saves available.")
    
    thing = input("Enter the name of the save to load or create: ").strip().lower()
    
    if thing in saves:
        print(f"Loading save: {thing}")
        playground.main(thing)
    else:
        print(f"Creating new save: {thing}")
        result = commands.make_save(thing)
        if result == "Success":
            playground.main(thing)
        else:
            print(f"Failed to create save: {result}")

if __name__ == "__main__":
    main()
