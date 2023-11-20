from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS


import recognize
# import translate


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/recognize/voice", methods=["POST"])
def transcription():
    print(request.get_data())
    print("request test")

    data_voice = request.get_data()
    path = 'input.wav'
    f = open(path, 'wb')
    f.write(data_voice)
    f.close()
    
    result = recognize.transcribe_audio(path)
    print(result)
    return jsonify({"text": result}), 200

# @app.route("/translate/voice", method=["POST"])
# def trans():
#     # data_text = request.files['files']
#     input_str = request.get_json()["key"]
#     translate.tranlate()
#     input_json = jsonify(input_str)
#     return recognize.transcribe_audio(input_json), 200
