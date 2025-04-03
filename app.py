from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample chatbot logic
def chatbot_response(user_input):
    if "sad" in user_input.lower() or "depressed" in user_input.lower():
        return "I'm really sorry to hear that. I'm here to listen. 💙"
    elif "help" in user_input.lower():
        return "You're not alone. I'm here to talk. What’s on your mind? 🤖"
    elif "thank" in user_input.lower():
        return "You're welcome! I'm always here for you. 💙"
    else:
        return "I hear you. Can you tell me more about how you're feeling? 💙"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_text = request.args.get("msg")
    response = chatbot_response(user_text)
    return jsonify({"bot_response": response})

if __name__ == "__main__":
    app.run(debug=True)
