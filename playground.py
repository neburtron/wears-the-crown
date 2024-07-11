import os
import llm_interface
import commands
import random

instruct = commands.read_file("prompt.txt")
runForTurns = 10
currentTurn = 0
fileNum = 0
currentState = ""

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def main(save):
    global currentTurn, savePath, currentState, fileNum
    savePath = f"saves/{save}"
    
    if not os.path.exists(savePath):
        print(f"Error: Save path '{savePath}' does not exist.")
        return
    
    for turn in range(runForTurns):
        currentTurn += 1
        manageItems(savePath)


def manageItems(save_path):
    global fileNum, currentTurn
    
    turnPath = f"{save_path}/{currentTurn-1}"

        
    if not os.path.exists(turnPath):
        print(f"Error: Directory '{turnPath}' does not exist. Skipping turn {currentTurn-1}.")
        return
    
    for i in os.listdir(turnPath):
        file_path = os.path.join(turnPath, i)
        if os.path.isfile(file_path):  # Check if it's a file
            content = commands.read_file(file_path)
            generate(content)


def generate(content):
    global currentState, instruct
    currentState1 = currentState
    
    if currentState == "":
        currentState = content
        return
    else:
        array = [
            {"role": "system", "content": instruct},
            {"role": "user", "content": currentState},
            {"role": "user", "content": content}
        ]
        print(instruct)
        print(currentState)
        print(content)
        randomChoice = random.choice([0, 1])
        if randomChoice == 1:
            pass
        else:
            currentState = content
    
    response = llm_interface.main(array)
    print(response.content)
    
    deal_w_response(response, currentState1, content)

def deal_w_response(response, one, two):
    global fileNum, savePath
    
    if response is None:
        # Handle the case where no valid response was received
        print("Error: No valid response received.")
        return
    
    content = getattr(response, 'content', None)
    if not content:
        print("Error: Response content is empty or invalid.")
        return
    
    current_turn_path = f"{savePath}/{currentTurn}"
    create_directory(current_turn_path)
    
    file_path = f"{current_turn_path}/{fileNum}.txt"
    commands.save_txt(file_path, content)
    
    file_path_source = f"{current_turn_path}/source/"

    create_directory(file_path_source)
    commands.save_txt(file_path_source + "/input" + str(fileNum) + ".txt", one + "\n\n\n" + two)
    fileNum += 1
