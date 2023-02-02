from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from controller import process
import json
from pathlib import Path

app = Flask(__name__)
CORS(app)


@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello World</p>"


@app.route("/fetchExample", methods=["GET", "POST"])
@cross_origin()
def fetchExample():
    positiveDataPath = Path("../server/data/positiveData.json")
    negativeDataPath = Path("../server/data/negativeData.json")

    if not positiveDataPath.is_file() or not negativeDataPath.is_file():
        process()

    positiveJson = open(positiveDataPath, "r")
    negativeJson = open(negativeDataPath, "r")

    jsonFile = json.load(positiveJson)
    resp = jsonify(wordCount=jsonFile)

    return resp


if __name__ == "__main__":
    app.run(port=3100, debug=True)
    # fetchExample()
