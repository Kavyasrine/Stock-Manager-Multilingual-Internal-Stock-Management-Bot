from .connection import get_conn
from datetime import datetime

def get_product_by_name(name: str):
    with get_conn() as conn:
        cur = conn.execute('SELECT * FROM products WHERE LOWER(name)=LOWER(?)', (name,))
        row = cur.fetchone()
        return dict(row) if row else None

def list_products():
    with get_conn() as conn:
        cur = conn.execute('SELECT * FROM products')
        return [dict(r) for r in cur.fetchall()]

def create_product(name, quantity=0, threshold=0, supplier=None):
    with get_conn() as conn:
        cur = conn.execute('INSERT OR IGNORE INTO products (name, quantity, threshold, supplier, last_updated) VALUES (?, ?, ?, ?, ?)',
                           (name, quantity, threshold, supplier, datetime.utcnow().isoformat()))
        return get_product_by_name(name)

def update_quantity(name, delta):
    with get_conn() as conn:
        p = get_product_by_name(name)
        if not p:
            return None
        new_qty = max(0, p['quantity'] + delta)
        conn.execute('UPDATE products SET quantity=?, last_updated=? WHERE id=?', (new_qty, datetime.utcnow().isoformat(), p['id']))
        return get_product_by_name(name)

def set_threshold(name, threshold):
    with get_conn() as conn:
        p = get_product_by_name(name)
        if not p:
            return None
        conn.execute('UPDATE products SET threshold=?, last_updated=? WHERE id=?', (threshold, datetime.utcnow().isoformat(), p['id']))
        return get_product_by_name(name)