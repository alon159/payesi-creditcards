# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from app.config import config_by_name
from app.routes import register_routes
from flask_cors import CORS

db = SQLAlchemy()
api = Api()

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    CORS(app)
    
    db.init_app(app)
    
    # Import and register blueprints/routes
    register_routes(api)
    api.init_app(app)

    # Print registered routes for debugging
    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule.rule}")
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app