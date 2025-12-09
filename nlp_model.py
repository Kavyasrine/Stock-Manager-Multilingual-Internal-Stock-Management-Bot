import spacy

# Load English model safely
try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = None

def parse(text: str):
    """
    Parse text using spaCy if available.
    Otherwise fallback to basic rules.
    """
    if nlp:
        return nlp(text)
    return None


def extract_entities(text: str):
    """
    Extract product name & quantity using simple rules.
    No dependency on spaCy model (safe fallback).
    """

    text_low = text.lower()

    # --- Quantity extraction ---
    quantity = None
    for word in text_low.split():
        if word.isdigit():
            quantity = int(word)
            break

    # --- Product extraction ---
    # simple rule: take longest word that is not a number
    words = [w for w in text_low.split() if not w.isdigit()]
    product = max(words, key=len) if words else None

    # Clean product (remove symbols)
    if product:
        product = product.replace(".", "").replace(",", "")

    # Override with spaCy noun_chunks if model exists
    if nlp:
        doc = nlp(text)
        try:
            noun_chunks = [chunk.text for chunk in doc.noun_chunks]
            if noun_chunks:
                product = noun_chunks[0].strip().lower()
        except:
            pass

    return {
        "product": product,
        "quantity": quantity
    }
