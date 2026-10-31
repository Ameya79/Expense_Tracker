from datetime import datetime
from typing import Tuple, Optional


def validate_expense_input(date_str: str, amount_str: str, category_str: str, note_str: str) -> Tuple[bool, Optional[str], Optional[float]]:
    """
    Validate expense form inputs.
    Returns: (is_valid, error_message, parsed_amount)
    """
    # Validate date
    if not date_str or not date_str.strip():
        return False, "Date cannot be empty.", None
    try:
        datetime.strptime(date_str.strip(), "%Y-%m-%d")
    except ValueError:
        return False, "Date must be in valid YYYY-MM-DD format.", None

    # Validate amount
    if not amount_str or not amount_str.strip():
        return False, "Amount cannot be empty.", None
    try:
        amount = float(amount_str.strip())
        if amount <= 0:
            return False, "Amount must be a positive number greater than zero.", None
        if amount > 1_000_000_000:
            return False, "Amount exceeds reasonable threshold ($1,000,000,000).", None
    except ValueError:
        return False, "Amount must be a valid numeric value.", None

    # Validate category
    category = category_str.strip() if category_str else ""
    if not category:
        return False, "Category cannot be empty.", None
    if len(category) > 100:
        return False, "Category name must be under 100 characters.", None

    # Validate note
    note = note_str.strip() if note_str else ""
    if len(note) > 500:
        return False, "Note must be under 500 characters.", None

    return True, None, round(amount, 2)
