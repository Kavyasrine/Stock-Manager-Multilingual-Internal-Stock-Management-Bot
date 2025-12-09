 Stock Manager — FastAPI Inventory System

A lightweight inventory management system built using **FastAPI**, **SQLite**, and **Pydantic**.
This project allows you to **add, update, delete, search, and list products** with clean architecture and modular code.
**Features**

**Core Functionalities**

* Add new products
* Update existing products
* Delete products
* Fetch product by ID
* Fetch all products
* Search products by name or category
* Automatic database initialization with sample data

### **Technical Stack**

* **Backend Framework:** FastAPI
* **Database:** SQLite (products.db)
* **ORM:** Custom minimal DB wrapper
* **Validation:** Pydantic
* **Server:** Uvicorn

---

## **📁 Project Structure**

```
Stock Manager/
│── app/
│   ├── main.py               # FastAPI application and routes
│   ├── models.py             # Pydantic models
│   ├── connection.py         # Database connection + CRUD operations
│   ├── classifier.py         # Optional logic classifier
│   ├── bot_logic.py          # High-level logic (optional)
│   └── __init__.py
│── products.db               # Auto-created SQLite database
│── README.md                 # Project documentation
```

---

## **🔧 Installation & Setup**

### **1. Install dependencies**

```bash
pip install fastapi uvicorn pydantic
```

### **2. Run the FastAPI server**

```bash
python -m uvicorn app.main:app --reload
```

### **3. Access API documentation**

* Open your browser
* Type:

```
http://127.0.0.1:8000/docs
```

This opens the **Swagger UI** where you can test all endpoints easily.

---

## **🗄️ Database**

* SQLite database file: `products.db`
* Automatically created on the first run
* Preloaded with sample product data

Database schema:

```
id INTEGER PRIMARY KEY AUTOINCREMENT
name TEXT NOT NULL
category TEXT
price REAL
quantity INTEGER
```

---

## **📌 API Endpoints Overview**

### **Product**

| Method | Endpoint                       | Description         |
| ------ | ------------------------------ | ------------------- |
| GET    | `/products`                    | Fetch all products  |
| GET    | `/product/{product_id}`        | Fetch product by ID |
| POST   | `/add-product`                 | Add new product     |
| PUT    | `/update-product/{product_id}` | Update product      |
| DELETE | `/delete-product/{product_id}` | Delete product      |

---

## **📘 Example Request**

### **POST — Add product**

```json
{
  "name": "Laptop Bag",
  "category": "Accessories",
  "price": 899.50,
  "quantity": 10
}
```

---

## **🧩 Code Flow Explanation**

### **1. main.py (Router Layer)**

Handles all routes and connects them to database functions.

### **2. connection.py (Database Layer)**

Contains:

* SQLite connection
* Table creation
* CRUD operations

### **3. models.py (Data Validation)**

Defines Pydantic models for request/response.

## **🚀 Future Enhancements**

* JWT authentication
* Admin dashboard UI
* Barcode scanning integration
* Role-based access
* Stock alert notifications


Just tell me, chellom.
