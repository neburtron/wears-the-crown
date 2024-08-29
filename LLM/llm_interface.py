from LLM.openai_client import OpenAIClient
from LLM.huggingface_client import HuggingFaceClient
import src.utils as utils
import LLM.last_tab_index as LT

class LLMInterface:
    def __init__(self):
        self.client = None
        self.initialize_client()

    def initialize_client(self):
        settings_folder = "./settings"
        tab_index = LT.get_last_tab_index(settings_folder)        
        if tab_index == 0:
            settings = utils.load_json(f"{settings_folder}/OpenAI")
            self.client = OpenAIClient(settings)
        elif tab_index == 1:
            settings = utils.load_json(f"{settings_folder}/HuggingFace")
            self.client = HuggingFaceClient(settings)

    def get_response(self, msgs):
        if self.client:
            try:
                return self.client.get_response(msgs)
            except Exception as e:
                print(f"Error during LLM interaction: {e}")
                return None
        else:
            print("No client initialized.")
            return None
        