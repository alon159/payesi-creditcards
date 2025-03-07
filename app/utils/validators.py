# app/utils/validators.py
def validate_card_data(data):
    """
    Validate credit card data
    
    Returns:
        dict or None: Error response if validation fails, None if validation passes
    """
    # Check required fields
    required_fields = ['card_number', 'expiry_month', 'expiry_year', 'cardholder_name']
    for field in required_fields:
        if field not in data:
            return {"error": f"Missing required field: {field}"}, 400
    
    # Validate card number (basic check)
    if not data['card_number'].isdigit() or len(data['card_number']) < 13 or len(data['card_number']) > 19:
        return {"error": "Invalid card number format"}, 400
    
    # Validate expiry date
    if not data['expiry_month'].isdigit() or int(data['expiry_month']) < 1 or int(data['expiry_month']) > 12:
        return {"error": "Invalid expiry month"}, 400
    
    if not data['expiry_year'].isdigit() or len(data['expiry_year']) != 4:
        return {"error": "Invalid expiry year"}, 400
    
    # Additional validations can be added here
    
    return None