from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, template_folder="D:\Mini Project\Age")

# Function to get exchange rates
def get_exchange_rate(from_currency, to_currency):
    API_URL = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(API_URL).json()
    return response["rates"].get(to_currency, None)

@app.route("/")
def index():
    return render_template("Currency.html")

@app.route("/convert", methods=["POST"])
def convert():
    data = request.json
    from_currency = data["from"]
    to_currency = data["to"]
    amount = float(data["amount"])

    rate = get_exchange_rate(from_currency, to_currency)
    
    if rate is None:
        return jsonify({"error": "Invalid currency"}), 400
    
    converted_amount = amount * rate
    return jsonify({"converted": round(converted_amount, 2)})

if __name__ == "__main__":
    app.run(debug=True)
