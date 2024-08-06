"""
    List Choices arguments:
    
choices - list of options that already exist
preamble - text that goes before the input
text1 - text that goes before the list of choices in list_items
text2 - text that does before user input in choice
unrestricted - if any choice works or just one from list - bool (True or False)
"""
def list_choices(choices, preamble, text1, text2, unrestricted):
    list_items(choices, text1, unrestricted)
    return choice(choices, text2, preamble, unrestricted)

def list_items(choices, text, unrestricted):
    print("\n" + text + "\n")
    if choices:
        for choice in choices:
            print(f"- {choice}")
    elif not unrestricted:
        print("\n\n"  +  "No items in list of valid options: error, error, error."  +  "\n\n")
        exit()
    else:
        print("No items in list.")

def choice(choices, text, preamble, unrestricted):
    print("\n" + text + "\n")
    prompt = f"{preamble}: " if preamble else ""
    user_choice = input(prompt).strip().lower()
    
    if not unrestricted:
        if user_choice in choices:
            return user_choice
        else:
            print("\nInvalid input, try again.\n")
            return choice(choices, text, preamble, False)
    else:
        return user_choice