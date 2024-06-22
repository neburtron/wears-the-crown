import os
import llm_interface
import commands

def main(thing):
    run_instance = Run(thing)
    run_instance.main()

class Run:

    def __init__(self, thing) -> None:
        self.array = []
        self.instruct = commands.read_file("prompt.txt")
        self.thing = thing
        self.turns_to_run = 10
        save_path = f"saves/{self.thing}"
        
        if not os.path.exists(save_path):
            os.makedirs(save_path)
            self.passed_turns = 0
        else:
            self.passed_turns = len(os.listdir(save_path))
        
        if self.passed_turns > 0:
            self.turn = commands.load_json(f"{save_path}/{self.passed_turns - 1}/file.json")['turn']
        else:
            print("Start the thing off.\n\n\n")
            self.turn = input()

    def array_input(self, role, msg):
        self.array.append({"role": role, "content": msg})

    def main(self):
        for turn in range(self.turns_to_run):
            self.array.clear()
            self.array_input("system", self.instruct)
            self.array_input("user", self.turn)
            
            print(self.array)
        
            response = llm_interface.main(self.array)
        
            self.deal_w_response(response)
        
            self.passed_turns += 1
            save_path = f"saves/{self.thing}/{self.passed_turns}"
            if not os.path.exists(save_path):
                os.makedirs(save_path)
        
            # Assuming self.turn is updated to be a string in deal_w_response
            commands.save_txt(f"{save_path}/file.txt", {"turn": self.turn})


    
    def deal_w_response(self, response):
        if response is None:
            # Handle the case where no valid response was received
            print("Error: No valid response received.")
            return

        # Implement the response handling logic here
        print(f"Response: {response}")
    
        # Assuming the response object has a 'content' attribute and other attributes you need to serialize
        #serializable_response = {
            #"content": response.content,
            #"role": response.role,
            # Include any other attributes of the response you need
            # "function_call": response.function_call,
            # "tool_calls": response.tool_calls,
        #}

        # Assuming the turn is updated here based on the response
        self.turn = response.content  # Modify this according to your actual logic

        # Save the serializable response instead of the raw response object
        save_path = f"saves/{self.thing}/{self.passed_turns}"
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        commands.save_txt(f"{save_path}/file.txt", response.content)
