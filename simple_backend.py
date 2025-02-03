import os
from dotenv import load_dotenv
from together import Together

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT", "")

MODEL_NAME = "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo"

client = Together(api_key=TOGETHER_API_KEY)

# Maintain a conversation history in memory
conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}]

def chat_with_llm(user_message: str):
    # Add the user message to the conversation history
    conversation_history.append({"role": "user", "content": user_message})

    # Generate a response based on the conversation history
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=conversation_history,
    )

    # Get the AI's response and add it to the conversation history
    ai_message = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": ai_message})

    return ai_message

if __name__ == "__main__":
    print("Welcome to the conversation with Rabbi Snow! Type 'exit' to quit.")
    
    while True:
        print("This is the beginning of your conversation with Rabbi Snow. Type 'exit' to end the conversation.")
        user_input = input("\nYou: ")
        
        if user_input.lower() == "exit":
            print("Rabbi Snow out. Goodbye")
            break
        
        print("Rabbi Snow:")
        response = chat_with_llm(user_input)
        print(response)
