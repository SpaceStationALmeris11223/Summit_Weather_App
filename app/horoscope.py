#app/horoscope.py
import requests
import os

API_KEY = os.getenv("P2KgqKXqCM9UZ2foof32w4bOLzPhVNjA9M9le5hP")

def get_horoscope(sign, day="today"):
    url = "https://freeastrologyapi.com/api-docs"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = {
        "sign": sign.lower(),
        "day": day
    }

    response = requests.post(url, json=payload, headers=headers)
    
    print("Status Code:", response.status_code)
    print("Raw Response Text:", response.text)
    
    try:
        return response.json()
    except Exception as e:
        return {"description": "Error fetching horoscope"}