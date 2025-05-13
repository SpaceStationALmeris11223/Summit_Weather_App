from app import create_app
from flask import Flask, Blueprint
# ↑Loads the app code
app = create_app()


if __name__ == "__main__":
# ↑ only runs if it's the main file
#starts the app ↓ in debug mode
    app.run(debug=True)