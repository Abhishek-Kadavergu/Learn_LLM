from openai import OpenAI
import os
from app.core.config import OPEN_ROUTER_API_KEY

client = OpenAI(
    api_key=OPEN_ROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


def generate_response(prompt: str):

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=500
    )

    return response.choices[0].message.content