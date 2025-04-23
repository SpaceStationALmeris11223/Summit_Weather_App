#Thsi files will pull flask and other relavant tools
from flask import Flask
# ↓ allows the app to use a database
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
#↑ Allows the app to read hidden values from a .env file(Api Keys, passwords, etc.)
import os
#↑ Allows the app to interact with your operating system
db = SQLAlchemy()
#↑ creates a database object
def create_app():
    load_dotenv()
#looks for ↑ file called .env adn loads any key value pairs
    app = Flask(__name__)
    app.config.from_object('config.Config')#←Loads config settings
    db.init_app(app)#←connects app to database

    from .routes import main
#    ↑imports the routes Aka different pages(urls)
#   ↓plugs in (connects) the recently imported routes to the app
    app.register_blueprint(main)
    return app