import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def ask_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()
