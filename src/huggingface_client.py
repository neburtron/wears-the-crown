from huggingface_hub import InferenceApi

class HuggingFaceClient:
    def __init__(self, settings):
        self.client = InferenceApi(
            repo_id=settings['model'],
            token=settings['api_key'],
            api_url=settings.get('base_url', 'https://api-inference.huggingface.co')
        )
        
    def get_response(self, msgs):
        response = self.client(inputs=msgs)
        return response.get('generated_text')
