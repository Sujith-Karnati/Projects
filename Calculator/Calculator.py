from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="D:\Mini Project\Age")

@app.route("/")
def index():
    return render_template("Calculator.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    operation = data["operation"]

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2 if num2 != 0 else "Error (Division by zero)"
    else:
        result = "Invalid Operation"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
