import os
import pytest
import tempfile
import pandas as pd
from app import app
import expense_store
from validators import validate_expense_input


@pytest.fixture
def client(monkeypatch):
    """Create a temporary CSV file and configured test client."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_csv = os.path.join(tmpdir, "test_expenses.csv")
        monkeypatch.setattr(expense_store, "CSV_FILE", test_csv)
        expense_store.init_csv()

        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        with app.test_client() as client:
            yield client


def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Financial Dashboard" in response.data
    assert b"Total Expenses" in response.data


def test_add_get_route(client):
    response = client.get("/add")
    assert response.status_code == 200
    assert b"New Expense" in response.data
    assert b"Amount" in response.data


def test_add_post_valid(client):
    response = client.post("/add", data={
        "date": "2026-10-31",
        "amount": "45.50",
        "category": "Groceries",
        "note": "Weekly market trip"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Expense added successfully!" in response.data
    assert b"Groceries" in response.data
    assert b"45.50" in response.data


def test_add_post_invalid_amount(client):
    response = client.post("/add", data={
        "date": "2026-10-31",
        "amount": "-10.00",
        "category": "Food",
        "note": "Negative"
    })
    assert response.status_code == 400
    assert b"positive number" in response.data


def test_add_post_invalid_date(client):
    response = client.post("/add", data={
        "date": "invalid-date",
        "amount": "20.00",
        "category": "Food",
        "note": "Bad date"
    })
    assert response.status_code == 400
    assert b"YYYY-MM-DD" in response.data


def test_view_route(client):
    response = client.get("/view")
    assert response.status_code == 200
    assert b"Expense Log" in response.data


def test_delete_expense(client):
    # Add an expense first
    client.post("/add", data={
        "date": "2026-10-31",
        "amount": "100.00",
        "category": "Transport",
        "note": "Train pass"
    })
    assert len(expense_store.get_all_expenses()) == 1

    # Delete index 0
    del_resp = client.post("/delete/0", follow_redirects=True)
    assert del_resp.status_code == 200
    assert b"Expense entry removed." in del_resp.data
    assert len(expense_store.get_all_expenses()) == 0


def test_clear_expenses(client):
    # Add two expenses
    client.post("/add", data={"date": "2026-10-30", "amount": "20", "category": "Food", "note": ""})
    client.post("/add", data={"date": "2026-10-31", "amount": "30", "category": "Travel", "note": ""})
    assert len(expense_store.get_all_expenses()) == 2

    # Clear
    clear_resp = client.post("/clear", follow_redirects=True)
    assert clear_resp.status_code == 200
    assert b"All expenses have been reset successfully." in clear_resp.data
    assert len(expense_store.get_all_expenses()) == 0


def test_download_csv(client):
    response = client.get("/download")
    assert response.status_code == 200
    assert response.headers["Content-Disposition"].startswith("attachment")
    assert b"date,amount,category,note" in response.data


def test_custom_404_page(client):
    response = client.get("/nonexistent-endpoint-404")
    assert response.status_code == 404
    assert b"Page Not Found" in response.data


def test_validators():
    valid, err, val = validate_expense_input("2026-10-31", "99.95", "Shopping", "Shoes")
    assert valid is True
    assert err is None
    assert val == 99.95

    valid, err, val = validate_expense_input("", "10", "Cat", "")
    assert valid is False
    assert "Date cannot be empty" in err

    valid, err, val = validate_expense_input("2026-10-31", "abc", "Cat", "")
    assert valid is False
    assert "valid numeric value" in err
