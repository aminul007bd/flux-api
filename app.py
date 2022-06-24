
from flask import Flask, jsonify, Response, Request
import requests



app = Flask(__name__)

ACCESS_KEY = 'V6m3vwqx7XXBcA7Mxfvfxnkc291IhIKgJwYrZcqe'
url = str.__add__('https://api.currencyapi.com/v3/latest?apikey=', ACCESS_KEY) 


@app.route("/hello")
def hello() -> Response:
    """Simple example of an API endpoint"""
    return jsonify({"message": "ohai"})


@app.route("/hello/<string:name>")
def hello_name(name: str) -> Response:
    """Simple example using an URL parameter"""
    return jsonify({"message": "ohai {}".format(name)})


# Latest Exchange Rates for USD,GBP,EUR
@app.route("/latest")
def latest_rates() -> Response:
    latest_rates = url + '&currencies=USD,GBP,EUR'
    response = requests.get(latest_rates)


    return jsonify({"message": format(response.json())})


# Convert currency depends on base currency and round up to decimal position two
@app.route("/convert/<string:base_curr>/<string:curr>")
def convert_currency(base_curr: str, curr: str) -> Response:
    convert_rates = url + '&base_currency='+ base_curr + '&currencies=' + curr
  
    data = requests.get(convert_rates).json()
    curr_value = data["data"][curr]["value"]
    curr_value = round(curr_value, 2)

    return jsonify({"message": format(data)})

