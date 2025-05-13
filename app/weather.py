# Import necessary modules
import requests

# Function to fetch weather data from an external API
def fetch_weather_from_api(location):
    # Placeholder URL for the weather API
    api_url = f"https://api.weather.com/v3/weather/{location}"
    # Send a GET request to the API
    response = requests.get(api_url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        weather_data = response.json()
        # Return the weather data
        return weather_data
    else:
        # Return an error message if the request failed
        return {'error': 'Failed to fetch weather data'}

# Function to process and format weather data
def process_weather_data(raw_data):
    # Extract relevant fields from the raw data
    location = raw_data.get('location', 'Unknown')
    temperature = raw_data.get('temperature', 'N/A')
    condition = raw_data.get('condition', 'N/A')
    # Format the data into a dictionary
    formatted_data = {
        'location': location,
        'temperature': temperature,
        'condition': condition
    }
    # Return the formatted data
    return formatted_data
