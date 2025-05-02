from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("index.html")
    return app

# ↑Loads the app code
app = create_app()

if __name__ == "__main__":
# ↑ only runs if it's the main file
#starts the app ↓ in debug mo
    app.run(debug=True)

