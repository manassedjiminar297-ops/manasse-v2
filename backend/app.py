import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

GEMINI_KEY = os.getenv("GEMINI_KEY")

@app.get("/")
def home():
    return {"status": "Manasse V2 International OK"}

@app.get("/ask")
def ask(q: str):
    if not GEMINI_KEY:
        return {"error": "GEMINI_KEY not set on Render"}
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
    r = requests.post(url, json={"contents": [{"parts": [{"text": q}]}]})
    try:
        text = r.json()["candidates"][0]["content"]["parts"][0]["text"]
        return {"answer": text}
    except Exception as e:
        return {"error": str(e), "raw": r.text}

