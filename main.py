import commands
import select_llm_details
import playground

print("Welcome!\n\n")

def main():
    print("Do you want to change LLM settings? (write Y for yes, N for no)")
    choose = input().strip().upper()
    
    if choose == "Y":
        select_llm_details.run_llm_settings()
    elif choose != "N":
        print("Invalid input. Exiting...")
        return
    
    saves()
    

def saves():
    saves = commands.list_saves()
    
    for save in saves:
        print(f"\n{save}\n")
        
    thing = input().strip().lower()
    if thing in saves:
        playground.main(thing)
    else:
        commands.make_save(thing)
    



if __name__ == "__main__":
    main()