# app/routes/credit_card_routes.py
from flask import request, jsonify
from flask_restful import Resource
from app.models import CreditCard
from app import db
from app.services.tokenization_service import tokenize_card
from app.utils.validators import validate_card_data

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
        cardToken, cvvToken, dniToken = tokenize_card(data['cardNumber'], data['cvv'], data['dni'])
        
        new_card = CreditCard(
            cardNumber=cardToken,
            cardHolderName=data['cardHolderName'],
            expirationDate=data['expirationDate'],
            cvv=cvvToken,
            type=data['type'],
            active=data['active'],
            dni=dniToken,
        )
        
        db.session.add(new_card)
        db.session.commit()
        
        return new_card.to_dict(), 201