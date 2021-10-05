import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import route
from .config import config, init_config


def test_app():
    app = Flask(__name__)

    route(app)

    path = os.environ.get('CONFIG_PATH') if os.environ.get(
        'CONFIG_PATH') else "./settings.ini"
    init_config(path)

    try:
        app.config.update(dict(
            SECRET_KEY=str(config['FLASK_APP']['FLASK_APP_SECRET_KEY'])
        ))
        app.config.update(dict(
            SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL", "sqlite://")
        ))
        app.config.update(dict(
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        ))
        print(f"\n\033[32m Сервер запустился с конфигом:\n\033[32m {path}\n")
        db = SQLAlchemy(app)
    except KeyError:
        print(f"\033[31m Файл {path} не найден или неверный")

    return app
