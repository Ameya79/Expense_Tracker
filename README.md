# 💸 Modern Flask & Bootstrap 5 Expense Tracker

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.x-black.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3.svg?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Docker](https://img.shields.io/badge/docker-ready-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![Tests](https://img.shields.io/badge/pytest-passing-success.svg?logo=pytest&logoColor=white)](https://pytest.org/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)

A standardized, production-ready **Expense Tracker** web application built with **Flask**, **Pandas**, and **Bootstrap 5**. Upgraded from a minimal prototype into a responsive financial management dashboard equipped with interactive data visualizations, real-time filtering, robust input validation, containerization, and unit tests.

---

## 🌟 Key Features

- 📊 **Executive Dashboard**:
  - Real-time aggregate metric cards: **Total Spent**, **Transaction Count**, **Top Category**, and **Average Expense**.
  - **Spending Distribution**: Interactive Chart.js doughnut chart and visual category percentage breakdown bars.
  - **Daily Spending Trend**: Recent volume timeline bar chart.
- ➕ **Structured Expense Entry**:
  - Bootstrap 5 floating form controls with client-side & server-side validation.
  - Preset categories (Food & Dining, Groceries, Transportation, Utilities, Entertainment, Health & Fitness, Shopping, Travel, Education) + custom category option.
  - Safe decimal amounts with bounds checking ($0.01 to $1,000,000,000).
  - Post-Redirect-Get (PRG) pattern preventing duplicate submissions.
- 📋 **Interactive Expense Log (`/view`)**:
  - Live client-side keyword search across dates, categories, and notes.
  - Category filter dropdown with instant table re-rendering.
  - Row-level deletion with Bootstrap confirmation modal.
- 📥 **Reliable CSV Persistence**:
  - Automatic directory and header initialization.
  - Error-resilient export endpoint (`/download`) with graceful fallback.
  - Clear all records modal with confirmation safeguards.
- 🐳 **Containerized & Production Ready**:
  - Multi-stage lightweight `python:3.12-slim` Dockerfile with non-root security.
  - Docker Compose service definition with automated healthchecks and volume persistence.
  - Gunicorn WSGI server.
- 🧪 **Comprehensive Test Suite**:
  - Pytest coverage verifying routes, input validation, CSV data operations, error handling, and edge cases.

---

## 📂 Project Architecture

```
Expense_Tracker/
├── app.py                  # Main Flask application & route controllers
├── expense_store.py        # Abstracted CSV data access layer & statistics engine
├── validators.py           # Form input validation & sanitization
├── requirements.txt        # Production Python dependencies
├── Dockerfile              # Production container build definition
├── docker-compose.yml      # Orchestration with healthcheck & volume mounts
├── .dockerignore           # Build context optimization rules
├── .env.example            # Environment configuration template
├── README.md               # Standardized documentation
├── templates/              # Standardized Jinja2 Bootstrap 5 templates
│   ├── base.html           # Base layout, navbar, flash alerts, confirmation modal
│   ├── index.html          # Executive dashboard & Chart.js visualizations
│   ├── add.html            # New expense form with validation
│   ├── view.html           # Filterable expense log & delete controls
│   ├── 404.html            # Custom 404 error page
│   └── 500.html            # Custom 500 error page
└── tests/
    └── test_app.py         # Pytest test suite (11 unit & integration tests)
```

---

## 🚀 Quickstart Guide

### Option 1: Run with Docker Compose (Recommended)

Ensure [Docker](https://docs.docker.com/get-docker/) is installed, then launch:

```bash
# Clone the repository
git clone https://github.com/Ameya79/Expense_Tracker.git
cd Expense_Tracker

# Start the application in detached mode
docker compose up -d
```

Open your browser and navigate to:
👉 **[http://localhost:5000](http://localhost:5000)**

To view logs or stop the service:
```bash
docker compose logs -f
docker compose down
```

---

### Option 2: Run Locally with Python

**Prerequisites:** Python 3.10+ and `pip`

```bash
# 1. Clone repository
git clone https://github.com/Ameya79/Expense_Tracker.git
cd Expense_Tracker

# 2. (Optional) Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run application
python app.py
```

The app will be accessible at **[http://localhost:5000](http://localhost:5000)**.

---

## 🌐 Routes & Endpoints

| Route | Method | Description |
|---|---|---|
| `/` | `GET` | **Dashboard**: Financial overview, metrics, charts & recent items |
| `/add` | `GET`, `POST` | **Add Expense**: Render form / Submit validated expense record |
| `/view` | `GET` | **Log View**: Filterable table of all recorded expenses |
| `/delete/<int:index>` | `POST` | **Delete Expense**: Delete individual record by row index |
| `/download` | `GET` | **Export**: Download `expenses.csv` file |
| `/clear` | `GET`, `POST` | **Reset**: Clear all data while retaining CSV schema headers |

---

## 🧪 Running Automated Tests

Run the complete test suite with `pytest`:

```bash
pytest tests/ -v
```

All 11 test cases verify:
- Root and subpage HTTP 200 responses
- Input validation (negative amounts, non-numeric strings, bad date formats)
- CSV write, read, and delete operations
- CSV export attachment headers
- Custom 404 and error boundaries

---

## ⚙️ Environment Variables

Copy `.env.example` to `.env` to configure custom runtime options:

```bash
PORT=5000                                            # Port to bind
SECRET_KEY=your_secure_secret_key_here               # Session & flash message key
FLASK_ENV=production                                 # Environment mode
EXPENSES_CSV=expenses.csv                            # Custom path to CSV storage file
```

---

## 👤 Author & Contributions

- **Author**: Ameya Kulkarni
- **Upgrades & Standardization**: Modernized to Bootstrap 5, Docker Compose, and automated testing.
- **License**: MIT
