from app import create_app
# ↑Loads the app code
app = create_app()

if __name__ == "__main__":
# ↑ only runs if its the main file
#starts the app ↓ in debug mo
    app.run(debug=True)
