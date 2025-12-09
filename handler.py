# app/handler.py
from langdetect import detect
from googletrans import Translator

translator = Translator()

LANGUAGE_ALIASES = {
    'ta': 'ta',
    'en': 'en',
    'ml': 'ml'
}


def detect_language(text: str) -> str:
    try:
        lang = detect(text)
        return lang
    except Exception:
        return 'en'


def translate_to_english(text: str, src: str=None) -> (str, str):
    # returns (translated_text, detected_source)
    try:
        if not src:
            src = detect_language(text)
        if src == 'en':
            return text, 'en'
        res = translator.translate(text, src=src, dest='en')
        return res.text, src
    except Exception:
        # fallback: return original
        return text, src or 'en'


def translate_from_english(text: str, dest: str) -> str:
    try:
        if dest == 'en':
            return text
        res = translator.translate(text, src='en', dest=dest)
        return res.text
    except Exception:
        return text