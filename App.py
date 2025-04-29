# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application instance
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    # Render the index.html template for the home page
    return render_template('index.html')

# Define the route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve username and password from the form
        username = request.form['username']
        password = request.form['password']
        # Redirect to the home page after login (placeholder logic)
        return redirect(url_for('home'))
    # Render the login.html template for the login page
    return render_template('login.html')

# Run the application if this script is executed
if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)
