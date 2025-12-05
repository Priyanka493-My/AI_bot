from fastapi import FastAPI
from pydantic import BaseModel
from memory_extractor import extract_memory
from personality_engine import apply_personality
import uvicorn

app = FastAPI()

class MessageRequest(BaseModel):
    messages : list[str]
    personality : str
    user_input : str

@app.post("/process/")
def process(data: MessageRequest):
    memory = extract_memory(data.messages)
    base_reply = f"Based on what you said:{data.user_input}"
    reply_with_personality = apply_personality(base_reply,data.personality)
    return {"memory": memory, "reply_with_personality": reply_with_personality}

