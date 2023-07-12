from app import create_app, db
from Server.Models.user import Users
from config import app_config

config_name = "development"

def seed_data(config_name):
    app = create_app(config_name)
    with app.app_context():
        user1 = Users(username='john_doe', email='john@example.com', password='Passw0rd')
        user2 = Users(username='jane_smith', email='jane@example.com', password='Passw0rd')
        # Add more seed data here

        db.session.add(user1)
        db.session.add(user2)
        # Add more seed data to the session

        db.session.commit()

if __name__ == '__main__':
    seed_data(config_name)
