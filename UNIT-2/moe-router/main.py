import os
from groq import Groq
from dotenv import load_dotenv

from router import route_prompt
from experts import MODEL_CONFIG

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def process_request(user_input):

    # Step 1: route to expert
    category = route_prompt(user_input)

    print(f"Routed to: {category}")

    if category not in MODEL_CONFIG:
        category = "general"

    config = MODEL_CONFIG[category]

    # Step 2: call expert model
    response = client.chat.completions.create(
        model=config["model"],
        temperature=config["temperature"],
        messages=[
            {"role": "system", "content": config["system_prompt"]},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    while True:

        user_input = input("\nEnter your query (or 'exit'): ")

        if user_input.lower() == "exit":
            break

        answer = process_request(user_input)

        print("\nResponse:")
        print(answer)
