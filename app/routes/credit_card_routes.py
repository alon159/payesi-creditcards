# app/routes/credit_card_routes.py
from flask import request, jsonify
from flask_restful import Resource
from app.models import CreditCard
from app import db
#from app.services.tokenization_service import tokenize_card
from app.utils.validators import validate_card_data, compare_data
import random

#/api/cards/<string:card_id>
class CreditCardResource(Resource):
    def get(self, card_id):
        card = CreditCard.query.get_or_404(card_id)
        return jsonify(card.to_dict())
    
    def delete(self, card_id):
        card = CreditCard.query.get_or_404(card_id)
        db.session.delete(card)
        db.session.commit()
        return '', 204

#/api/cards
class CreditCardListResource(Resource):
    def get(self):
        cards = CreditCard.query.all()
        return jsonify([card.to_dict() for card in cards])
    
    def post(self):
        data = request.get_json()
        
        # Validate the data
        validation_error = validate_card_data(data)
        if validation_error:
            return validation_error
        
        # Tokenize card data
        #cardToken, cvvToken, dniToken = tokenize_card(data['number'], data['cvv'], data['user_dni'])
        
        new_card = CreditCard(
            number=data['number'],
            balance=round(random.uniform(0, 10000),2),
            card_holder_name=data['card_holder_name'],
            expiration_date=data['expiration_date'],
            cvv=data['cvv'],
            type=data['type'],
            active=True,
            user_dni=data['user_dni'],
        )
        
        db.session.add(new_card)
        db.session.commit()
        
        return new_card.to_dict(), 201
    
#/api/cards/validate
class CreditCardValidationResource(Resource):
    def post(self):
        data = request.get_json()
        creditCard = CreditCard.query.get_or_404(data['number'])

        return compare_data(data, creditCard.to_dict())
    
#/api/cards/charge
class CreditCardChargeAuthorizationResource(Resource):
    def put(self):
        data = request.get_json()
        creditCard = CreditCard.query.get_or_404(data['number'])
        amount = data['amount']

        if creditCard.balance < amount:
            return {"error": "Insufficient funds"}, 400
        
        creditCard.balance -= amount
        db.session.commit()

        return '', 200