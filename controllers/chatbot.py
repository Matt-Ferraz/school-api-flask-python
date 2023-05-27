import os
import openai
from dotenv import load_dotenv

load_dotenv();
class ChatBot:
    messages = []
    api_key = os.getenv("OPEN_AI_KEY")

    def __init__(self):
        openai.api_key = self.api_key

    def send_message(self, message):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            
            messages= message
        )   
        assistant_reply = response['choices'][0]['message']['content']
        self.messages.append({
            "role": "system",
            "content": assistant_reply
        })
        return assistant_reply
