# app/weather.py

import requests
import os

def get_weather(latitude, longitude):
    base_url = os.getenv('WEATHER_API_URL')

    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current': 'temperature_2m,is_day,wind_speed_10m,wind_direction_10m,rain,showers,snowfall,weather_code',
        'daily': 'weather_code,temperature_2m_max,temperature_2m_min',
        'timezone': 'auto',
        'temperature_unit': 'fahrenheit',
        'wind_speed_unit': 'mph',
        'precipitation_unit': 'inch',
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data  # now returns full current + daily
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        if e.response is not None:
            print(f"Response text: {e.response.text}")
        return None
