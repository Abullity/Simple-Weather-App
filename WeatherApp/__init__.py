import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
secret = secrets.token_urlsafe(32)
app.secret_key = secret
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
db = SQLAlchemy(app)


from WeatherApp import models, routes


db.create_all()
db.session.commit()
