from app import create_app


app = create_app()

if __name__ == "__main__":
# ↑ only runs if it's the main file
#starts the app ↓ in debug mode
    app.run(debug=True)