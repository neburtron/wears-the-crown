from src.openai_client import OpenAIClient
from src.huggingface_client import HuggingFaceClient
from src.settings_manager import get_settings, get_last_tab_index

class LLMInterface:
    def __init__(self):
        self.client = None
        self.initialize_client()

    def initialize_client(self):
        tab_index = get_last_tab_index()
        if tab_index == 0:
            settings = get_settings("OpenAI")
            self.client = OpenAIClient(settings)
        elif tab_index == 1:
            settings = get_settings("HuggingFace")
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