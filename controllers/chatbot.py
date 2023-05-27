import openai

class ChatBot:
    messages = []
    api_key = "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"

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
