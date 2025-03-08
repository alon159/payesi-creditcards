# Flask Credit Card API

A secure backend API for managing credit card information built with Flask.

## Features

- RESTful API endpoints for storing and retrieving credit card information
- Secure tokenization of sensitive data
- Modular project structure for easy maintenance and scaling

## Tech Stack

- Flask
- SQLAlchemy
- Flask-RESTful

## Installation

1. Clone the repository:
   git clone https://github.com/your-username/flask-credit-card-api.git
   cd flask-credit-card-api
2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
3. Install dependencies:
   pip install -r requirements.txt
4. Create a .env file with your configuration variables.
5. Run the application:
   python run.py

## API Endpoints

- `GET /api/cards` - Get all cards
- `POST /api/cards` - Create a new card
- `GET /api/cards/<card_id>` - Get a specific card
- `DELETE /api/cards/<card_id>` - Delete a card

## Security Note

This project is for demonstration purposes. In production, consider:

- Using a PCI-compliant payment processor
- Implementing proper authentication and authorization
- Enabling HTTPS for all connections
