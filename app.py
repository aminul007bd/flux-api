from flask import Flask, jsonify, Response


app = Flask(__name__)


@app.route("/hello")
def hello() -> Response:
    """Simple example of an API endpoint"""
    return jsonify({"message": "ohai"})


@app.route("/hello/<string:name>")
def hello_name(name: str) -> Response:
    """Simple example using an URL parameter"""
    return jsonify({"message": "ohai {}".format(name)})
