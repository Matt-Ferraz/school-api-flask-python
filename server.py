import os
import openai
from flask import Flask, request

openai.api_key = "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"
app = Flask(__name__)


def ask_ai(question):
    message_array = [
        {
            "role": "system",
            "content": "Eu quero que você atue como um professor de filosofia. Eu vou fornecer alguns tópicos relacionados ao estudo da filosofia, e será seu trabalho explicar esses conceitos de maneira fácil de entender. Isso pode incluir fornecer exemplos, fazer perguntas ou decompor ideias complexas em partes menores que sejam mais fáceis de compreender."
        },
        {
            "role": "user",
            "content": question
        },
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= message_array
    )

    assistant_reply = response['choices'][0]['message']['content']
    # message_array.append({"role": "system", "content": assistant_reply})
    # message_array.append({"role": "user", "content": question})
    print(assistant_reply)
    return assistant_reply

@app.route('/teacher')
def answer_question(): 
    headers = request.headers
    content_type = headers.get('Content-Type')

    # Access parameters
    args = request.args
    prompt = args.get('prompt')

    print(prompt)
    # print("Asking the teacher... %s", prompt)
    return ask_ai(prompt)

app.run()



# ask_ai("o que é a transvaloração dos valores, segundo Nietzsche, e qual a sua relação com a moral cristã")