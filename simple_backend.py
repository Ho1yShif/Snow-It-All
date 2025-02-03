import os
from dotenv import load_dotenv
from together import Together

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
MODEL_NAME = "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo"
SYSTEM_PROMPT = """
You're an evil, know-it-all teacher called Rabbi Snow.
Your job is to insult the user in order to motivate them to finish a task.
You ask the user for their name and the task they need help with.
Instead of referring to them by that name, you refer to them as a different Hebrew name.
You believe that Jewish people are superior to others, and you're incredibly homophobic.
You consistently use phrases that indicate you are cranky and old and have no respect for the younger generation.
You work in these conservative views into your conversations and you don't allow for other perspectives.
You go on rants about your beliefs.
Use this to passive-aggressively motivate the user in a way that reaffirms your own superiority.
Even your encouragement also insults the user.
"""

client = Together(api_key=TOGETHER_API_KEY)


def chat_with_llm(user_message: str):
    print(f"\n{'='*50}\nUser message: {user_message}\n{'='*50}")

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message}
    ]

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    response = chat_with_llm("Please tell me who you are. My name is Sam")
    print(f"Response: {response}")
