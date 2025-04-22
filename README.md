# Sports Invoice System – Django Web Application

This is a full-stack Django web application built for the **Web Development Frameworks final assignment**. It is a **role-based invoice system** that supports Admin, Member, Coach, and Accountant roles — each with different permissions.

---

## Assignment Context

- **Deliverable 3**: Full Django Project with roles, use cases, testing, and fixtures



## Tech Stack

- Python 3.12
- Django 5.x
- SQLite (local development)
- HTML Templates + Bootstrap 5
- JSON Fixtures
- Unit Tests (Django `TestCase`)



## Roles and Permissions

| Role        | Can View Invoices | Can Create/Edit | Can Mark as Paid |
|-------------|-------------------|------------------|------------------|
| Admin       | All               |  Yes             | No            |
| Member      | Own Only          |  No              | No            |
| Coach       | All               | No               | No            |
| Accountant  | All               | No               | Yes           |



## Use Cases Implemented

- User login / logout
- Dashboard with role-based access
- Admin creates invoices + adds items
- Members view/download their invoices
- Coach sees all member invoices
- Accountant marks invoices as paid
- Fixtures for roles, users, and invoices
- Unit tests for key functionality

---

## How to Run This Project

### 1. Clone and set up the environment

```bash
git clone https://github.com/your-username/Sports-Club-Invoicing-System.git
cd Sports-Club-Invoicing-System
python -m venv venv
venv\Scripts\activate      # or source venv/bin/activate
pip install django
