# app/models/credit_card.py
from app import db

class CreditCard(db.Model):
    number = db.Column(db.String(16), primary_key=True)
    balance = db.Column(db.Float, nullable=False)
    card_holder_name = db.Column(db.String(100), nullable=False)
    expiration_date = db.Column(db.String(5), nullable=False)
    cvv = db.Column(db.String(3), nullable=False)
    type = db.Column(db.String(12), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    user_dni = db.Column(db.String(12), nullable=False)

    def to_dict(self):
        return {
            "number": self.number,
            "card_holder_name": self.card_holder_name,
            "expiration_date": self.expiration_date,
            "cvv": self.cvv,
            "type": self.type,
            "active": self.active,
            "user_dni": self.user_dni,
        }
