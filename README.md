# 💸 Flask & Pandas Expense Tracker

[![Python](https://img.shields.io/badge/python-3.7%2B-blue)]()
[![Flask](https://img.shields.io/badge/flask-2.x-lightgrey)]()
[![Pandas](https://img.shields.io/badge/pandas-2.x-green)]()
[![License](https://img.shields.io/badge/license-MIT-orange)]()

A **simple web-based Expense Tracker** built with **Flask** and **Pandas** — perfect for beginners learning how to work with CSV files in Python.  
No CSS. No JavaScript. Just clean, functional HTML.

---

## 🚀 Features
- ➕ **Add Expense**: Log date, amount, category, and notes.
- 👀 **View Expenses**: See all your records in a neat table.
- 📥 **Download CSV**: Export all expenses in `.csv` format.
- 🗑️ **Clear All**: Reset the file while keeping headers.

---

## 🖼 Preview
*(Optional: Add screenshot of `/view` here)*

---

## 📂 Project Structure

├── app.py ├── expenses.csv └── templates/ └── add.html

---

## 🛠 Requirements
```bash
$ pip install flask pandas


---

▶️ How to Run

$ python app.py

Then visit http://localhost:5000/add


---

🌐 Routes

Route	Method	Description

/add	GET/POST	Add a new expense
/view	GET	View all recorded expenses
/download	GET	Download the CSV file of expenses
/clear	GET	Clear all saved expense records



---

🧼 Sample CSV

date,amount,category,note
2025-07-27,250,Groceries,Bought veggies
2025-07-27,500,Transport,Cab fare


---

📤 Deploy

Render: Push to GitHub → Create new web service → Set python app.py as start command.

Replit: Import the repo → Click "Run".



---

👤 Author

Ameya Kulkarni
💻 GitHub | 📫 LinkedIn | 🎯 Codolio

⭐ If you found this useful, consider starring the repo!

---
