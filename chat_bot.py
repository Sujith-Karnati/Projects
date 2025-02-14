from flask import Flask, render_template, request, jsonify

app = Flask(__name__,template_folder="D:\Mini Project\Age")

# Store student data
student_data = {}

@app.route("/")
def index():
    return render_template("Chat.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    user_input = data.get("message", "").lower()

    if "name" in user_input:
        student_data["name"] = user_input.split()[-1]
        return jsonify({"response": f"Got it! Your name is {student_data['name']}. What is your age?"})
    
    elif "age" in user_input:
        student_data["age"] = ''.join(filter(str.isdigit, user_input))
        return jsonify({"response": f"Thanks! Your age is {student_data['age']}. What is your email?"})
    
    elif "@" in user_input:
        student_data["email"] = user_input
        return jsonify({"response": f"Noted! Your email is {student_data['email']}. What course are you enrolling in?"})
    
    elif "course" in user_input:
        student_data["course"] = user_input.split()[-1]
        return jsonify({"response": f"Great! You are enrolling in {student_data['course']}. Thank you!"})
    
    else:
        return jsonify({"response": "I'm here to collect student details. What's your name?"})

if __name__ == "__main__":
    app.run(debug=True)
