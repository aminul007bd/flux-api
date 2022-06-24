
from flask import Flask, jsonify, Response, Request
import requests



app = Flask(__name__)

# api key
ACCESS_KEY = 'V6m3vwqx7XXBcA7Mxfvfxnkc291IhIKgJwYrZcqe'
# api url for rate conversion
url = str.__add__('https://api.currencyapi.com/v3/latest?apikey=', ACCESS_KEY) 


# Latest Exchange Rates for USD,GBP,EUR
@app.route("/latest")
def latest_rates() -> Response:
    latest_rates = str.__add__(url ,'&currencies=USD,GBP,EUR')
    data = requests.get(latest_rates).json()


    return jsonify({"Latest Exchange Rates In (USD, GBP, EUR)": format(data)})


# Convert currency depends on base currency and round up to decimal position two
@app.route("/convert/<string:base_curr>/<string:converted_curr>")
def convert_currency(base_curr: str, converted_curr: str) -> Response:
    convert_rates = url + '&base_currency=' + base_curr + '&currencies=' + converted_curr
  
    data = requests.get(convert_rates).json()
    curr_value = data["data"][converted_curr]["value"]
    curr_value = round(curr_value, 2)

    return jsonify({"Converted Rate ": format(data)})

