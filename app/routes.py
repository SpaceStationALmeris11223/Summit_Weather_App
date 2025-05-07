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

#app/horoscope.py

from flask import request
from .horoscope import get_horoscope

@main.route('/horoscope', methods=["GET","POST"])
def horoscope():
    sign = "aries"
    horoscope_data = {}

    if request.method == "POST":
        sign = request.form.get("sign")
        horoscope_data = get_horoscope(sign)
        print(horoscope_data)
    return render_template("horoscope.html", data=horoscope_data, sign=sign)
