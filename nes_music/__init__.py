from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nes_music.db"
db = SQLAlchemy(app)

# from nes_music import errors
from nes_music import models
from nes_music import routes
