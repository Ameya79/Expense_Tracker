import os
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from expense_store import (
    init_csv, get_all_expenses, add_expense_record,
    delete_expense_record, clear_all_expenses, get_expense_stats, CSV_FILE
)
from validators import validate_expense_input

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "expense_tracker_secret_dev_key_2024")

# Initialize CSV on startup
init_csv()


@app.route("/")
def index():
    """Root route: Redirect to view or render dashboard."""
    stats = get_expense_stats()
    expenses = get_all_expenses()
    return render_template("index.html", stats=stats, expenses=expenses)


@app.route("/add", methods=["GET", "POST"])
def expense_page():
    """Add a new expense record with validation and Post-Redirect-Get pattern."""
    if request.method == "POST":
        date = request.form.get("date", "")
        amount = request.form.get("amount", "")
        category = request.form.get("category", "")
        note = request.form.get("note", "")

        is_valid, error_msg, clean_amount = validate_expense_input(date, amount, category, note)
        if not is_valid:
            flash(error_msg, "danger")
            return render_template("add.html", date=date, amount=amount, category=category, note=note), 400

        add_expense_record(date, clean_amount, category, note)
        flash("Expense added successfully!", "success")
        return redirect(url_for("view"))

    return render_template("add.html")


@app.route("/view")
def view():
    """View all recorded expenses."""
    expenses = get_all_expenses()
    stats = get_expense_stats()
    return render_template("view.html", expenses=expenses, stats=stats)


@app.route("/download")
def csv_download():
    """Download the expenses CSV."""
    init_csv()
    return send_file(CSV_FILE, as_attachment=True, download_name="expenses.csv")


@app.route("/delete/<int:index>", methods=["POST"])
def delete_expense(index: int):
    """Delete a single expense by row index."""
    success = delete_expense_record(index)
    if success:
        flash("Expense entry removed.", "success")
    else:
        flash("Could not find expense entry to delete.", "warning")
    return redirect(url_for("view"))


@app.route("/clear")
def clear_expenses():
    """Clear all expenses."""
    clear_all_expenses()
    flash("All expenses have been cleared.", "info")
    return redirect(url_for("view"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
