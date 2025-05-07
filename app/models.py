from flask_sqlalchemy import    SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
#this files purpose is to help defin the  structure of the database.
#Classes that will represent tables will be created here.
db = SQLAlchemy()

#↓defines user as a class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
#stores hashed pword securely↑
#called during ↓registration to hash and store password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
#verifys entered pword↓ is stored as hash
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)