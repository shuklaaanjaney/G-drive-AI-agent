from fastapi import FastAPI
from pydantic import BaseModel

from agent import generate_query
from drive_tool import search_drive

app = FastAPI()

# Request body model
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Drive AI Agent Running"}

@app.post("/chat")
async def chat(req: ChatRequest):

    # Generate AI query
    query = generate_query(req.message)

    # Search Google Drive
    files = search_drive(query)

    return {
        "user_input": req.message,
        "generated_query": query,
        "files": files
    }