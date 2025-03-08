# app/services/tokenization_service.py
import hashlib

def tokenize_card(cardNumber, cvv, dni):
    """
    Tokenize a credit card number, CVV, and DNI.
    
    WARNING: This is a simple demo implementation.
    In production, use a PCI-compliant tokenization service.
    
    Returns:
        tuple: (number_token, cvv_token, dni_token)
    """
    # Simple tokenization - NOT for production use
    cardNumberToken = hashlib.sha256(cardNumber.encode()).hexdigest()
    cvvToken = hashlib.sha256(cvv.encode()).hexdigest()
    dniToken = hashlib.sha256(dni.encode()).hexdigest()
    
    return cardNumberToken, cvvToken, dniToken