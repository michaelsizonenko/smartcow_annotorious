from app import test_app
from models import db

if __name__ == "__main__":
    db.create_all()
    test_app().run(host='0.0.0.0')