# create_db.py
import sqlite3
from datetime import datetime


DB = 'products.db'


SCHEMA = """
CREATE TABLE IF NOT EXISTS products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT UNIQUE NOT NULL,
quantity INTEGER NOT NULL DEFAULT 0,
threshold INTEGER NOT NULL DEFAULT 0,
supplier TEXT,
last_updated TEXT
);


CREATE TABLE IF NOT EXISTS transactions (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_id INTEGER NOT NULL,
change INTEGER NOT NULL,
reason TEXT,
date TEXT,
FOREIGN KEY(product_id) REFERENCES products(id)
);
"""


SAMPLE = [
("Milk", 50, 10, "Local Dairy"),
("Soaps", 100, 20, "HygieneSuppliers"),
("Bread", 30, 5, "BakeryCo"),
]




def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.executescript(SCHEMA)
    for name, qty, thr, sup in SAMPLE:
        cur.execute("INSERT OR IGNORE INTO products (name, quantity, threshold, supplier, last_updated) VALUES (?, ?, ?, ?, ?)",
            (name, qty, thr, sup, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()
    print(f"Initialized {DB} with sample data.")


if __name__ == '__main__':
    init_db()