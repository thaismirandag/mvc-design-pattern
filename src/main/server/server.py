from flask import Flask
from  flask_cors import CORS
from src.models.sqlite.settings.connection import db_connetion_handler
from src.main.routes.pets_routes import pet_route_bp

db_connetion_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pet_route_bp)
