from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from controller import processExample

app = Flask(__name__)
CORS(app)

@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello World</p>"

@app.route("/fetchExample", methods=["GET", "POST"])
@cross_origin()
def fetchExample():
    if request.method == "GET": # handling GET request
        wordCount = processExample()
        resp = jsonify(wordCount=wordCount)
        print(resp)
        return resp
    else: # handling POST request, which is only effective when ExampleWithInteractions.vue is loaded
        wordCount = processExample()
        resp = jsonify(wordCount=wordCount)
        print(resp)
        return resp


if __name__ == "__main__":
    app.run(port=3100, debug=True)