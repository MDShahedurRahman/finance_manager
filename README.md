
# Personal Finance Manager (CLI)

A clean, MVC-style **Python CLI application** for managing personal finances.  
This project is designed as a **portfolio-ready backend project**, demonstrating structured design, separation of concerns, and incremental development through Git commits.

---

## 📌 Features

- Create and manage multiple accounts (Checking, Savings, etc.)
- Track income and expense transactions
- Categorize transactions (Income vs Expense)
- Automatic balance updates per account
- Generate financial reports
  - Total income
  - Total expenses
  - Net balance
  - Balance by category
- JSON-based persistence (no database required)
- Clean **MVC architecture**
- CLI-friendly and easy to extend

---

## 🧠 Why This Project

This project is intentionally more advanced than a basic CRUD tracker.  
It demonstrates:

- Real-world domain modeling
- Business logic inside controllers
- Separation of concerns using MVC
- Incremental development (50+ logical commits)
- File-based persistence similar to backend services

Perfect for:
- Python backend portfolios
- Interview discussion projects
- Git commit practice
- MVC architecture demonstration

---

## 🗂 Project Structure

```
finance_manager/
├── main.py
├── config.py
├── models/
│   ├── account.py
│   ├── transaction.py
│   └── category.py
├── controllers/
│   ├── account_controller.py
│   ├── transaction_controller.py
│   └── report_controller.py
├── views/
│   ├── main_view.py
│   └── report_view.py
└── data/
    ├── accounts.json
    ├── transactions.json
    └── categories.json
```

---

## 🧩 Architecture (MVC)

### Model
- `Account`
- `Transaction`
- `Category`

Handles data structures and business entities.

### View
- `MainView`
- `ReportView`

Responsible for displaying information to the CLI.

### Controller
- `AccountController`
- `TransactionController`
- `ReportController`

Contains business logic, validation, and persistence handling.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- No external libraries required

### Run the Application

```bash
python main.py
```

The app will:
- Create sample accounts
- Add income and expense transactions
- Display account balances
- Generate summary reports

---

## 📊 Sample Output

```
Accounts:
acc1: Checking - Balance: 2850
acc2: Savings - Balance: 4300

Transactions:
txn1 | Salary | 2000 | Monthly Salary
txn2 | Groceries | 150 | Grocery shopping

Total Income: 2500
Total Expense: 1350
Net Balance: 1150
```

---
