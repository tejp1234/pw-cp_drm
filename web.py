# web.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "I'm alive!", 200
