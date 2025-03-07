# app/services/tokenization_service.py
import hashlib

def tokenize_card(card_number):
    """
    Tokenize a credit card number
    
    WARNING: This is a simple demo implementation.
    In production, use a PCI-compliant tokenization service.
    
    Returns:
        tuple: (token, last_four_digits)
    """
    # Simple tokenization - NOT for production use
    card_token = hashlib.sha256(card_number.encode()).hexdigest()
    last_four = card_number[-4:]
    
    return card_token, last_four