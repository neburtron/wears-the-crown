import openai

class OpenAIClient:
    def __init__(self, settings):
        self.client = openai.OpenAI(
            base_url=settings.get('base_url'),
            api_key=settings['api_key']
        )
        self.model = settings['model']
        self.temperature = settings['temp']

    def get_response(self, msgs):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=msgs,
            temperature=self.temperature,
        )
        return completion.choices[0].message