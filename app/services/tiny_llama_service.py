
import ollama


# Initialize Ollama client
client = ollama.Client(
    host="http://localhost:11434"
)


def generate_response(prompt: str):

    response = client.generate(
        model="tinyllama:latest",
        prompt=prompt
    )

    return response.response
