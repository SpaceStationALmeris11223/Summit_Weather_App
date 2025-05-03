# app/routes.py

from flask import Blueprint, render_template, request
from .weather import get_weather
import requests

main = Blueprint('main', __name__)

def get_coordinates(location):
    # Default coordinates (Minneapolis)
    default_lat = 44.9778
    default_lon = -93.2650
    
    try:
        # Use Nominatim API to get coordinates
        url = f"https://nominatim.openstreetmap.org/search?q={location}&format=json"
        headers = {'User-Agent': 'SummitWeatherApp/1.0'}
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
        return default_lat, default_lon
    except:
        return default_lat, default_lon

@main.route('/', methods=['GET', 'POST'])
def home():
    # Default coordinates (Minneapolis)
    latitude = 44.9778
    longitude = -93.2650

    # If form is submitted, use the user's input
    if request.method == 'POST':
        location = request.form.get('location', '')
        if location:
            latitude, longitude = get_coordinates(location)

    weather_data = get_weather(latitude, longitude)

    return render_template('index.html', 
                         weather=weather_data,
                         latitude=latitude,
                         longitude=longitude)
