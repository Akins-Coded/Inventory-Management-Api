
# 📦 Inventory Management System API

A RESTful API designed to efficiently track and manage inventory data in real time. Built with **Django Rest Framework**, the system supports CRUD operations, low-stock alerting, and role-based access for inventory managers and stock controllers. This project demonstrates best practices in backend development, including authentication, optimized querying, and scalable API design.

## 🚀 Features

- 🧾 **Product Management** – Create, read, update, and delete inventory items.
- 📉 **Low-Stock Alerts** – Automatic alerts when item stock falls below minimum threshold.
- 🔐 **Role-Based Access** – Assign roles with specific permissions (Admin, Manager, Controller).
- 📊 **Real-time Stock Monitoring** – Up-to-date overview of stock levels.
- 🔄 **API-First Design** – Built for frontend integration and automation.

---

## ⚙️ Technologies Used

- **Python 3.12**
- **Django 5+**
- **Django REST Framework**
- **SQLite**
- **JWT Authentication**

---

## 📁 Project Structure

```
inventory_system/
├── inventory/           # App for managing inventory operations
├── users/               # App for user roles and authentication
├── core/                # Settings, configuration, and base utilities
├── tests/               # Automated tests for all endpoints and logic
├── requirements.txt     # Dependencies
├── manage.py            # Django entry point
└── README.md
```

---

## 🔐 Authentication & Permissions

This project uses **JWT (JSON Web Tokens)** for secure authentication. Users must log in and receive a token to access protected routes.

- Admin: Full access
- Manager: CRUD on items, view alerts
- Controller: View only

```bash
# Get Token
POST /api/token/

# Example Header
Authorization: Bearer <your_token_here>
```



## 📦 API Endpoints Overview

| Method | Endpoint                 | Description                        |
|--------|--------------------------|------------------------------------|
| GET    | /api/products/           | List all products                  |
| POST   | /api/products/           | Add a new product                  |
| GET    | /api/products/<id>/      | Retrieve product by ID             |
| PUT    | /api/products/<id>/      | Update product                     |
| DELETE | /api/products/<id>/      | Delete product                     |
| GET    | /api/alerts/             | Get low-stock alerts               |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL
- pip

### Setup

```bash
git clone https://github.com/Akins-Coded/inventory-management-api.git
cd inventory-management-api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 📊 Future Improvements

- ✅ Admin dashboard (React/Next.js frontend)
- 📦 Stock batch upload via CSV
- 🛠️ Webhook for auto-restocking
- 📈 Analytics & Reporting module

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact

**Akindipe Muheez Omogbolahan**  
📧 Email: [akindipemuheez@outlook.com](mailto:akindipemuheez@outlook.com)  
🌐 [Linktree](https://linktr.ee/akinscoded)  
🔗 [LinkedIn](https://www.linkedin.com/in/akinscoded)  
💻 [GitHub](https://github.com/Akins-Coded)

---

_This project is part of my Backend Engineering portfolio. Built with precision, security, and scalability in mind._
