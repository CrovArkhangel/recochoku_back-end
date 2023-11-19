from flask import Flask
from flask import request
from flask import make_response
from flask_cors import CORS

import recognize
import translate


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/recognize/voice", methods=["POST"])
def transcription():
    data_voice = request.files['files']
    return recognize.recognize(data_voice), 200

# @app.route("/translate/voice", method=["POST"])
# def translate():
    



    