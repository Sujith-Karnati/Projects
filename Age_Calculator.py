from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__, template_folder="D:\Mini Project\Age")

def calculate_age(birthdate: str) -> int:
    birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

@app.route("/", methods=["GET", "POST"])
def index():
    age = None
    if request.method == "POST":
        birthdate = request.form["birthdate"]
        age = calculate_age(birthdate)
    return render_template("Age_Calculator.html", age=age)

if __name__ == "__main__":
    app.run(debug=True)
