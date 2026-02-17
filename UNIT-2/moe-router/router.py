import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def route_prompt(user_input):

    routing_prompt = f"""
Classify this text into one category:
technical, billing, general

Return ONLY the category name.

Text:
{user_input}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=[
            {"role": "system", "content": "You are a classification system."},
            {"role": "user", "content": routing_prompt}
        ]
    )

    category = response.choices[0].message.content.strip().lower()

    return category
