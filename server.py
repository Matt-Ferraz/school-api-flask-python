import json
from flask import Flask, request
from controllers.chatbot import ChatBot

app = Flask(__name__)

ai_bot = ChatBot()  # Create a global instance of ChatBot

@app.route('/teacher')
def answer_question():
	headers = request.headers
	# content_type = headers.get('Content-Type')

	args = request.args
	prompt = args.get('prompt')
	array_data = json.loads(prompt)

	return ai_bot.send_message(array_data)

if __name__ == '__main__':
	app.run(port=8800)