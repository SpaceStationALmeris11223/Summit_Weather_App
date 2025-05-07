import os
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///summit_weather.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS =False 