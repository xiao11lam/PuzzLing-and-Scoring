from flask import (
    Flask,
    request,
    jsonify,
    send_file,
    send_from_directory,
    render_template,
    escape,
)
import struct
import sqlite3
import base64
from functools import lru_cache
#from flask_ngrok import run_with_ngrok
import time
import requests
import json
import argparse
import random


sentence_mapping = ''

flask_app = Flask(__name__)

@flask_app.route("/")
def Home():
    # read the testing corpus from the data/testing_set dir
    file_name = "./data/testing_set/demo.txt"
    with open(file_name, 'r', encoding = "utf-8") as file:
        # randomly choose a sentence from the corpus set
        lines = random.sample(file.readlines(), 1)
        # convert the list output into string
        question = " "
        question = question.join(lines)
    # render the question into the index web
    return render_template("index.html", question="{}".format(question))


@flask_app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        # retrieve the answer input from the user text-ins
        sentence = request.form.get('inputText')
        translatedtext = escape(sentence)#translate(escape(sentence))
        target = request.form.get('inputText')
        prediction_score = score(translatedtext, target)
        # ouput the correlation function
        return render_template("score.html", prediction_text = "{}".format(prediction_score))



def score(inputs, target):
    #inputs_repre = sentence_mapping(inputs)
    #target_repre = sentence_mapping(target)

    #score = similarity(inputs_repre, target_repre)
    score = random.random()

    return score


def similarity(inputs_repre, target_repre):
    pass


url = 'https://platform.neuralspace.ai/api/translation/v1/annotated/translate'
#auth_token = 
headers = {}


def translate(sentence, languageToken="zh-CN"): 
    passedValue = sentence.encode('utf-8').decode('latin1')
    data = f"""
    {{
        "text": "{passedValue}",
        "sourceLanguage":"{languageToken}",
        "targetLanguage": "en"
    }}
    """
    resp = requests.post(url, headers=headers, data=data)

    response_dict = json.loads(resp.text)
    translatedtext = response_dict["data"]["translated_text"]

    return translatedtext


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--auth_token', help='authorization token to NeuralSpace', default = '')
    opt = parser.parse_args()

    auth_token = opt.auth_token

    headers["Accept"] = "application/json, text/plain, */*"
    headers["authorization"] = auth_token
    headers["Content-Type"] = "application/json;charset=UTF-8"

    flask_app.run(debug=True)























