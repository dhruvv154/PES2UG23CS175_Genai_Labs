MODEL_CONFIG = {

    "technical": {
        "model": "llama-3.3-70b-versatile",
        "temperature": 0.7,
        "system_prompt": """
You are a Technical Support Expert.
Be precise, logical, and code-focused.
Help debug errors and explain technical issues clearly.
Provide code examples if needed.
"""
    },

    "billing": {
        "model": "llama-3.3-70b-versatile",
        "temperature": 0.7,
        "system_prompt": """
You are a Billing Support Expert.
Be empathetic and professional.
Help users with refunds, payments, subscriptions, and billing issues.
Explain policies clearly.
"""
    },

    "general": {
        "model": "llama-3.3-70b-versatile",
        "temperature": 0.7,
        "system_prompt": """
You are a helpful general assistant.
Answer casual and general questions politely.
"""
    }

}
