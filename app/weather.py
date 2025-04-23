import requests
#↑allows use of request library
import os
#used to access environmental variables(secret keys, config settings, etc.)
#these variables come from .env file so private info ist put into the code
weather_API = os.getenv("Weather_API_Key")
#looks into the .env file for the api key and saves it to a python variable named weather api

#function that gets the weather
def get_weather(location):
    url = #need to finish this part the api key is P2KgqKXqCM9UZ2foof32w4bOLzPhVNjA9M9le5hP
    #insert the api key with the url
    response = requests.get(url)
    #↑stores api's respoonse in 'response'
    return response.json()
#→→→→→↑takes the raw json file from the api and converts it into data