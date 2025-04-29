# Import necessary modules
import sqlite3

# Define the database file path
DB_FILE = 'db/summit_weather.sqlite'

# Function to connect to the database
def connect_db():
    # Establish a connection to the SQLite database
    conn = sqlite3.connect(DB_FILE)
    # Return the connection object
    return conn

# Function to create a table for weather data
def create_weather_table():
    # Connect to the database
    conn = connect_db()
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    # SQL command to create the weather table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL,
            temperature REAL NOT NULL,
            condition TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Function to insert weather data into the table
def insert_weather_data(location, temperature, condition):
    # Connect to the database
    conn = connect_db()
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    # SQL command to insert data into the weather table
    cursor.execute('''
        INSERT INTO weather (location, temperature, condition)
        VALUES (?, ?, ?)
    ''', (location, temperature, condition))
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Function to fetch all weather data from the table
def fetch_weather_data():
    # Connect to the database
    conn = connect_db()
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    # SQL command to select all data from the weather table
    cursor.execute('SELECT * FROM weather')
    # Fetch all rows from the result
    rows = cursor.fetchall()
    # Close the connection
    conn.close()
    # Return the fetched rows
    return rows