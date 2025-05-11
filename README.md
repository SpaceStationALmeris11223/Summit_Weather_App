# Summit Weather App

Summit Weather App is a Flask-based web application that provides current weather and weekly forecasts for any location. Users can register, log in, and view weather data with a modern, responsive interface. The app uses the Open-Meteo API and features secure user authentication and input validation.

## Features

- User registration and login with password hashing
- Profanity filtering for usernames and passwords
- Fetches current weather and 7-day forecast using Open-Meteo API
- Interactive map display (Leaflet.js)
- Responsive, modern UI with Bootstrap and custom CSS
- Flash messaging for user feedback

## Getting Started

### Prerequisites

- Python 3.10+
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```powershell
   git clone <your-repo-url>
   cd Summit_Weather_App
   ```
2. **Create a virtual environment (optional but recommended):**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
   _(If `requirements.txt` is missing, install Flask and other dependencies manually:)_
   ```powershell
   pip install flask flask_sqlalchemy python-dotenv better_profanity requests
   ```
4. **Set up environment variables:**
   - Copy `.env` file and set your API keys and secret key:
     ```
     WEATHER_API_URL=https://api.open-meteo.com/v1/forecast
     Weather_API_Key=YOUR_API_KEY
     SECRET_KEY=YOUR_SECRET_KEY
     ```

### Database Initialization

The app uses SQLite by default. The database will be created automatically on first run.

### Running the App

```powershell
python run.py
```

The app will be available at `http://127.0.0.1:5000/`.

## Project Structure

```
Summit_Weather_App/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── register.py
│   ├── routes.py
│   ├── weather.py
│   ├── static/
│   │   └── styles.css
│   └── templates/
│       ├── index.html
│       ├── login.html
│       ├── register.html
│       └── horoscope.html
├── config.py
├── main.py
├── run.py
├── .env
├── README.md
└── db/
    └── summit_weather.sqlite
```

## Environment Variables

- `WEATHER_API_URL`: Base URL for the weather API
- `Weather_API_Key`: Your Open-Meteo API key
- `SECRET_KEY`: Flask secret key for sessions

## License

This project is for educational purposes. Add a license if you plan to distribute.

## Author

- Avery Houston, Natasha Wright, Cristal Lopez, Candace Vogel, Webster Boeing

---

_Summit Weather App - MCTC Software Capstone Project_
