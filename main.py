# app/main.py

# main.py
from fastapi import FastAPI
from pydantic import BaseModel

from app.handler import detect_language, translate_to_english, translate_from_english
from app.bot_logic import handle_message


app = FastAPI(title="Multilingual Internal Stock Management Bot")


class Message(BaseModel):
    text: str


@app.post("/chat")
def chat(msg: Message):
    user_text = msg.text

    # 1. detect language
    src_lang = detect_language(user_text)

    # 2. translate to English
    eng_text, detected = translate_to_english(user_text, src_lang)

    # 3. bot logic
    reply_eng = handle_message(eng_text)

    # 4. translate back to user language
    final_reply = translate_from_english(reply_eng, detected)

    return {
        "user_language": detected,
        "reply": final_reply
    }


@app.get("/")
def root():
    return {"message": "Stock Bot Running!"}
