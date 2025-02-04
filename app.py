import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from together import Together

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT", "")
MODEL_NAME = "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo"

client = Together(api_key=TOGETHER_API_KEY)

# Maintain conversation history
conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}]

app = Flask(__name__)

def chat_with_llm(user_message: str):
    conversation_history.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=conversation_history,
    )
    ai_message = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": ai_message})
    return ai_message

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"error": "Empty message"}), 400
    ai_response = chat_with_llm(user_message)
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(debug=True)
