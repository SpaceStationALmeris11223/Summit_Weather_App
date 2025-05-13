from sqlalchemy import create_engine
from models import Base

# Create the SQLite database engine
engine = create_engine('sqlite:///summit_weather.sqlite')

# Create all tables in the database
Base.metadata.create_all(engine)

print("Database tables created successfully.")