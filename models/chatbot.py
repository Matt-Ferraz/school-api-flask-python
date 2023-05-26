import openai

class ChatBot:
    messages = []
    api_key = "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"

    def __init__(self):
        openai.api_key = self.api_key
        # self.messages.append({
        #     "role": "system",
        #     "content": "Eu quero que você atue como um professor de filosofia. Eu vou fornecer alguns tópicos relacionados ao estudo da filosofia, e será seu trabalho explicar esses conceitos de maneira fácil de entender. Isso pode incluir fornecer exemplos, fazer perguntas ou decompor ideias complexas em partes menores que sejam mais fáceis de compreender."
        # })

    def send_message(self, message):
        # self.messages.append({
        #     "role": "user",
        #     "content": message
        # })
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            
            messages= message
        )   
        assistant_reply = response['choices'][0]['message']['content']
        self.messages.append({
            "role": "system",
            "content": assistant_reply
        })
        print(self.messages)
        print(assistant_reply)
        return assistant_reply