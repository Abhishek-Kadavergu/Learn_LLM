from fastapi import FastAPI, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
# from app.services.tiny_llama_service import generate_response
from app.services.groq_service import generate_response
# from app.services.gemini_service import generate_response
# from app.services.openrouter_service import generate_response
# from app.services.deepseek_service import generate_response

app = FastAPI()


@app.get("/")
def home():
    return "Main menu"


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        result = generate_response(request.prompt)
        return ChatResponse(response=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))