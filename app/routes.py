# app/routes.py

from flask import Blueprint, render_template
from .weather import get_weather

main = Blueprint('main', __name__)

@main.route('/')
def home():
    latitude = 44.9778  # Example default: Minneapolis
    longitude = -93.2650

    weather_data = get_weather(latitude, longitude)

    return render_template('index.html', weather=weather_data)
