from openai import OpenAI
from app.core.config import DEEPSEEK_API_KEY

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)


def generate_response(prompt: str):

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant. Give clear and concise answers."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=500,
        stream=False
    )

    return response.choices[0].message.content