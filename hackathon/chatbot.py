from flask import Flask, render_hackathon, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flas(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_hackathon("report.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('mag')
    return str(english_bot.get_response(userText))


if __name__=='__main__':
    app.run()