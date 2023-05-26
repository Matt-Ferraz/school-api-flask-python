import json
import openai
from flask import Flask, request
from models.chatbot import ChatBot

openai.api_key = "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"
app = Flask(__name__)

ai_bot = ChatBot()  # Create a global instance of ChatBot

@app.route('/teacher')
def answer_question(): 
    headers = request.headers
    content_type = headers.get('Content-Type')

    # Access parameters
    args = request.args
    prompt = args.get('prompt')
    array_data = json.loads(prompt)

    return ai_bot.send_message(array_data)

app.run()