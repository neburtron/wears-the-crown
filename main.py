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
    
    for save in saves:
        print(f"\n{save}\n")
        
    thing = input("Enter the name of the save to load or create: ").strip().lower()
    if thing in saves:
        playground.main(thing)
    else:
        commands.make_save(thing)
        playground.main(thing)

if __name__ == "__main__":
    main()
