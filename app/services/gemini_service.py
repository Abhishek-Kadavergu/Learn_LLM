from google import genai
from app.core.config import GEMINI_API_KEY

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)


def generate_response(prompt: str):

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return interaction.output_text