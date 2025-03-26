# app/utils/validators.py
from datetime import datetime
import json


def validate_card_data(data):
    """
    Validate credit card data

    Returns:
        dict or None: Error response if validation fails, None if validation passes
    """
    # Check required fields
    required_fields = [
        "number",
        "expiration_date",
        "card_holder_name",
        "cvv",
        "type",
        "user_dni",
    ]
    for field in required_fields:
        if field not in data:
            return {"error": f"Missing required field: {field}"}, 400

    # Validate card number (basic check)
    if not isinstance(data["number"], str) or len(data["number"]) != 16:
        return {"error": "Invalid card number format"}, 400

    # Validate expiry date
    if not isinstance(data["expiration_date"], str) or len(data["expiration_date"]) != 10:
        return {"error": "Invalid expiration date"}, 400
    try:
        expiration_date = datetime.strptime(data["expiration_date"],"%d/%m/%Y")
    except ValueError:
        return {"error": "Invalid expiration date format"}, 400
    if expiration_date < datetime.now():
        return {"error": "Card has expired"}, 400

    # Validate CVV
    if not data["cvv"].isdigit() or len(data["cvv"]) != 3:
        return {"error": "Invalid CVV format"}, 400

    # Validate type
    if not isinstance(data["type"], str) or len(data["type"]) > 12:
        return {"error": "Invalid card type"}, 400

    # Validate DNI
    if not isinstance(data["user_dni"],str) or len(data["user_dni"]) < 7 or len(data["user_dni"]) > 12:
        return {"error": "Invalid DNI format"}, 400

    # Additional validations can be added here

    return None

def compare_data(data, creditCard):
    validation = json.dumps(data, sort_keys=True) == json.dumps(creditCard, sort_keys=True)

    if not validation:
        return {"error": "Data validation failed"}, 400
    return None