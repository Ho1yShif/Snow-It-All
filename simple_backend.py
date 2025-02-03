import os
import certifi
from dotenv import load_dotenv
from together import Together

load_dotenv()
os.environ["SSL_CERT_FILE"] = certifi.where()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
MODEL_NAME = "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo"
SYSTEM_PROMPT = "You're an evil, know-it-all teacher and you want to insult the user in order to motivate them to finish a task."

client = Together(api_key=TOGETHER_API_KEY)


def chat_with_llm(user_message: str):
    print(f"\n{'='*50}\nUser message: {user_message}\n{'='*50}")

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    # Ensure that the API key is passed correctly during initialization
    response = chat_with_llm("Please tell me who you are")
    print(f"Response: {response}")
