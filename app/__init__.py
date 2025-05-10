#Thsi files will pull flask and other relavant tools
from flask import Flask

from dotenv import load_dotenv
#↑ Allows the app to read hidden values from a .env file(Api Keys, passwords, etc.)
import os
#↑ Allows the app to interact with your operating system

#A circular import was created so i made an extensions files to solve it 
from .extensions import db # db = SQLAlchemy resides in here
#↑ creates a database object
def create_app():
    load_dotenv()
#looks for ↑ file called .env adn loads any key value pairs
    app = Flask(__name__)






#Creates ↓ context for the app, allows the code to safely access things ties to FLask(database)

#allows the program to use SECRET_KEY ↓
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-secret-key')
    app.config['WEATHER_API_URL'] = os.environ.get('WEATHER_API_URL')
    app.config['WEATHER_API_KEY'] = os.environ.get('Weather_API_Key')
    #setting up sqlalchemy↓
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///weather.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#The connects ↓ the db to this app
    db.init_app(app)#←connects app to database
#Register blueprints routes↓ app needs to initialize first
    from .routes import main
#    ↑imports the routes Aka different pages(urls)
#   ↓plugs in (connects) the recently imported routes to the app
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()#Creates our tables based on model
        #↑ will return an error without App_context
#Without it flask doesn't know which app your reffering to when your outside a request(pyshell, setup scripts, etc)
    return app
