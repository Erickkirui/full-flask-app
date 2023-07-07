import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import app_config

# Create the SQLAlchemy db instance
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize the db with the app
    db.init_app(app)

    migrate = Migrate(app, db)

    with app.app_context():
        # Import the models here to ensure they are registered with SQLAlchemy
        from Server.Models.user import Users
        # Create the database tables (if they don't exist)
        db.create_all()

    from Server.Views import Version_one
    app.register_blueprint(Version_one)

    return app
