# 💸 Flask & Pandas Expense Tracker

A simple web-based Expense Tracker built using **Flask** and **Pandas**, with a plain HTML frontend. It allows you to add, view, download, and clear expense records saved in a CSV file.

---

## 🚀 Features

* ➕ **Add Expense**: Fill out a form to log date, amount, category, and notes.
* 👀 **View Expenses**: Displays all your recorded expenses in a clean HTML table.
* 📥 **Download CSV**: Exports all your expenses as a downloadable `.csv` file.
* 🗑️ **Clear All**: Clears all entries and resets the CSV with just the column headers.

---

## 🖼️ Frontend

Built using only **HTML** — no CSS, no JavaScript. Simple and functional.

---

## 📁 Project Structure

```
├── app.py               # Main Flask application
├── expenses.csv         # CSV file where data is stored (auto-created)
└── templates/
    └── add.html         # HTML form to input new expense
```

---

## 🛠️ Requirements

* Python 3.7+
* Flask
* Pandas

Install dependencies using:

```bash
pip install flask pandas
```

---

## ▶️ How to Run

```bash
python app.py
```

Then open your browser and go to:

```
http://localhost:5000/add
```

---

## 🌐 Routes Overview

| Route       | Method   | Description                       |
| ----------- | -------- | --------------------------------- |
| `/add`      | GET/POST | Add a new expense                 |
| `/view`     | GET      | View all recorded expenses        |
| `/download` | GET      | Download the CSV file of expenses |
| `/clear`    | GET      | Clear all saved expense records   |

---

## 🧼 Sample `expenses.csv`

```csv
date,amount,category,note
2025-07-27,250,Groceries,Bought veggies
2025-07-27,500,Transport,Cab fare
```

---

## 🧠 Notes

* Expenses are saved in a local `expenses.csv` file.
* The file is auto-created on the first entry.
* Only the `/add` route uses an HTML template — others return HTML via Flask.

---

## 📤 Deploy

You can deploy this app for free using platforms like **Render** or **Replit**.

