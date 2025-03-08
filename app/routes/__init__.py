# app/routes/__init__.py

def register_routes(api):
    # Import routes
    from app.routes.credit_card_routes import CreditCardResource, CreditCardListResource
    
    # Register routes
    api.add_resource(CreditCardListResource, '/api/cards')
    api.add_resource(CreditCardResource, '/api/cards/<string:card_id>')