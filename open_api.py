from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

# System helps set the tone for the Assistant. It is optional
# User will provide requests or comments for the assistant to respond to. Kinda like the regular API
# Assistant are model responses
env = load_dotenv(find_dotenv())
connect = OpenAI()
connect.api_key = os.getenv("OPENAI_API_KEY")


class Api:

    def __init__(self, message, model):
        self._message = message
        self._model = model

    def get_message(self):
        return self._message()

    def set_message(self, new: str):
        self._message = new

    def send_message(self):
        response = connect.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a unbiased assistant."},
                {"role": "user", "content": f"{self.get_message()}"},
            ]
        )

        return response.choices[0].message.content
