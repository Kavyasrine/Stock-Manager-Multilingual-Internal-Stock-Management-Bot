# app/predictor.py
from .db.transactions import get_transactions_for

def predict_restock_need(product_name, days=7):
    tx = get_transactions_for(product_name, limit=200)
    usage = [abs(t['change']) for t in tx if t['change'] < 0]
    if not usage:
        return 0
    avg_daily = sum(usage) / max(1, len(usage))
    suggested = int(max(0, avg_daily * days))
    return suggested

def check_threshold_and_recommend(product):
    suggested = predict_restock_need(product['name'])
    shortfall = max(0, product['threshold'] - product['quantity'])
    return {
        'product': product['name'],
        'quantity': product['quantity'],
        'threshold': product['threshold'],
        'shortfall': shortfall,
        'suggest_restock': suggested
    }
