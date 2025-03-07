# app/models/credit_card.py
from app import db
import uuid
from datetime import datetime

class CreditCard(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    card_token = db.Column(db.String(64), nullable=False, unique=True)
    last_four = db.Column(db.String(4), nullable=False)
    expiry_month = db.Column(db.String(2), nullable=False)
    expiry_year = db.Column(db.String(4), nullable=False)
    cardholder_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'last_four': self.last_four,
            'expiry_month': self.expiry_month,
            'expiry_year': self.expiry_year,
            'cardholder_name': self.cardholder_name,
            'created_at': self.created_at.isoformat()
        }