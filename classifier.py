# app/classifier.py
# A simple rule-based intent parser as MVP. Replace with DistilBERT fine-tune later.
import re

INTENTS = ['check_stock', 'add_stock', 'remove_stock', 'set_threshold', 'list_products', 'unknown']


def rule_intent(text: str):
    t = text.lower()
    if re.search(r"\b(add|increase|plus|add\s+stock)\b", t):
        return 'add_stock'
    if re.search(r"\b(remove|deduct|decrease|minus|sell)\b", t):
        return 'remove_stock'
    if re.search(r"\b(threshold|alert|set threshold|set alert)\b", t):
        return 'set_threshold'
    if re.search(r"\b(list|all products|show products)\b", t):
        return 'list_products'
    if re.search(r"\b(how many|stock|quantity|iruka|entha)\b", t):
        return 'check_stock'
    return 'unknown'