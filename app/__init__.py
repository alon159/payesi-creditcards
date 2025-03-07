# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from app.config import config_by_name

db = SQLAlchemy()
api = Api()

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    db.init_app(app)
    api.init_app(app)
    
    # Import and register blueprints/routes
    from app.routes import register_routes
    register_routes(api)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app