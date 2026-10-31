import os
import pandas as pd
from typing import Dict, Any, List, Optional

CSV_FILE = os.environ.get("EXPENSES_CSV", os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.csv"))
CSV_COLUMNS = ["date", "amount", "category", "note"]


def init_csv() -> None:
    """Ensure the CSV file exists with proper headers."""
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=CSV_COLUMNS)
        df.to_csv(CSV_FILE, index=False)


def get_expenses_df() -> pd.DataFrame:
    """Read expenses into a DataFrame, returning an empty DataFrame if file is missing."""
    init_csv()
    try:
        df = pd.read_csv(CSV_FILE)
        # Ensure required columns exist
        for col in CSV_COLUMNS:
            if col not in df.columns:
                df[col] = pd.NA
        # Clean amount as numeric
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0.0)
        return df
    except Exception:
        return pd.DataFrame(columns=CSV_COLUMNS)


def get_all_expenses() -> List[Dict[str, Any]]:
    """Return all expenses as a list of dicts with 0-based index."""
    df = get_expenses_df()
    records = []
    for idx, row in df.iterrows():
        records.append({
            "id": idx,
            "date": str(row["date"]) if pd.notna(row["date"]) else "",
            "amount": float(row["amount"]) if pd.notna(row["amount"]) else 0.0,
            "category": str(row["category"]) if pd.notna(row["category"]) else "General",
            "note": str(row["note"]) if pd.notna(row["note"]) else ""
        })
    return records


def add_expense_record(date: str, amount: float, category: str, note: str) -> None:
    """Append a single expense record to the CSV."""
    init_csv()
    new_expense = pd.DataFrame([{
        "date": date,
        "amount": round(float(amount), 2),
        "category": category.strip(),
        "note": note.strip()
    }])
    new_expense.to_csv(CSV_FILE, mode="a", index=False, header=not os.path.exists(CSV_FILE) or os.stat(CSV_FILE).st_size == 0)


def delete_expense_record(index: int) -> bool:
    """Delete a single expense by index."""
    df = get_expenses_df()
    if 0 <= index < len(df):
        df = df.drop(df.index[index])
        df.to_csv(CSV_FILE, index=False)
        return True
    return False


def clear_all_expenses() -> None:
    """Clear all records from the CSV file while preserving the column headers."""
    df = pd.DataFrame(columns=CSV_COLUMNS)
    df.to_csv(CSV_FILE, index=False)


def get_expense_stats() -> Dict[str, Any]:
    """Calculate aggregate metrics and category distribution."""
    df = get_expenses_df()
    if df.empty or len(df) == 0:
        return {
            "total_amount": 0.0,
            "total_count": 0,
            "average_amount": 0.0,
            "top_category": "None",
            "category_totals": {},
            "recent_expenses": []
        }

    total_amount = float(df["amount"].sum())
    total_count = int(len(df))
    average_amount = round(total_amount / total_count, 2) if total_count > 0 else 0.0

    category_grouped = df.groupby("category")["amount"].sum().to_dict()
    sorted_categories = sorted(category_grouped.items(), key=lambda x: x[1], reverse=True)
    top_category = sorted_categories[0][0] if sorted_categories else "None"

    return {
        "total_amount": round(total_amount, 2),
        "total_count": total_count,
        "average_amount": average_amount,
        "top_category": top_category,
        "category_totals": category_grouped,
        "recent_expenses": get_all_expenses()[-5:][::-1]
    }
