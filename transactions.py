# app/transactions.py
from .connection import get_conn
from datetime import datetime
from .products import get_product_by_name

def log_transaction(product_name, change, reason=None):
    p = get_product_by_name(product_name)
    if not p:
        return None
    with get_conn() as conn:
        conn.execute('INSERT INTO transactions (product_id, change, reason, date) VALUES (?, ?, ?, ?)',
                     (p['id'], change, reason or '', datetime.utcnow().isoformat()))
    return True

def get_transactions_for(product_name, limit=50):
    p = get_product_by_name(product_name)
    if not p:
        return []
    with get_conn() as conn:
        cur = conn.execute('SELECT * FROM transactions WHERE product_id=? ORDER BY date DESC LIMIT ?', (p['id'], limit))
        return [dict(r) for r in cur.fetchall()]