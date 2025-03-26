# app/services/tokenization_service.py
import hashlib

def tokenize_card(number, cvv, user_dni):
    """
    Tokenize a credit card number, CVV, and DNI.
    
    WARNING: This is a simple demo implementation.
    In production, use a PCI-compliant tokenization service.
    
    Returns:
        tuple: (number_token, cvv_token, dni_token)
    """
    # Simple tokenization - NOT for production use
    numberToken = hashlib.sha256(number.encode()).hexdigest()
    cvvToken = hashlib.sha256(cvv.encode()).hexdigest()
    dniToken = hashlib.sha256(user_dni.encode()).hexdigest()
    
    return numberToken, cvvToken, dniToken