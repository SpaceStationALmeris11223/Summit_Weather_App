
# Import necessary modules

import requests
#↑allows use of request library
import os
from dotenv import load_dotenv
#used to access environmental variables(secret keys, config settings, etc.)
#these variables come from .env file so private info ist put into the code
load_dotenv()
#looks into the .env file for the api key and saves it to a python variable named weather api
#bug fix
BASE_URL = os.getenv("WEATHER_API_URL")
""" 
#function that gets the weather
def get_weather(location):
    #url = #need to finish this part the api key is P2KgqKXqCM9UZ2foof32w4bOLzPhVNjA9M9le5hP
    #insert the api key with the url
    response = requests.get(url)
    #↑stores api's respoonse in 'response'
    return response.json()
#→→→→→↑takes the raw json file from the api and converts it into data
 """

# Function to fetch weather data from an external API

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        print("weather data recived", data)
        return data  # now returns full current + daily
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        if e.response is not None:
            print(f"Response text: {e.response.text}")
        return None
