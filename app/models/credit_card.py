# app/models/credit_card.py
from app import db

class CreditCard(db.Model):
    cardNumber = db.Column(db.String(16), primary_key=True)
    cardHolderName = db.Column(db.String(100), nullable=False)
    expirationDate = db.Column(db.String(5), nullable=False)
    cvv = db.Column(db.String(3), nullable=False)
    type = db.Column(db.String(12), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    dni = db.Column(db.String(12), nullable=False)

    def to_dict(self):
        return {
            "number": self.cardNumber,
            "cardHolderName": self.cardHolderName,
            "expirationDate": self.expirationDate,
            "cvv": self.cvv,
            "type": self.type,
            "active": self.active,
            "dni": self.dni,
        }
