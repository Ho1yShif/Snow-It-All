import os
import requests
from flask import Flask, render_template, request, jsonify, send_from_directory
from dotenv import load_dotenv
from together import Together

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT", "")
MODEL_NAME = "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo"

client = Together(api_key=TOGETHER_API_KEY)

conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}]

app = Flask(__name__, static_folder="static")


def chat_with_llm(user_message: str):
    conversation_history.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=conversation_history,
        )
        ai_message = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": ai_message})
        return ai_message

    except requests.exceptions.RequestException as e:
        print(f"Together AI request failed: {e}")
        return "Unfortunately, your request to Rabbi Snow has errored because your message was too idiotic. Please try again, and use your brain this time."

    except Exception as e:
        print(f"Unexpected error: {e}")
        return (
            "Unfortunately, your request to Rabbi Snow has errored. Please try again."
        )


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


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
