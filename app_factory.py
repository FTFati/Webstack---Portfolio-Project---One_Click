from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

# Create the Flask app instance
app = Flask(__name__)

# Configure the SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'

# Set the secret key for session security
app.config['SECRET_KEY'] = '2ef3acf95fb4dd67a3705440c55a548a2968e67b661baf2d'

# Initialize SQLAlchemy to work with the Flask app
db = SQLAlchemy(app)

# Configure email settings for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'fatima.amkachou@gmail.com'
app.config['MAIL_PASSWORD'] = 'FTFATI_2024'

# Initialize Flask-Mail to work with the Flask app
mail = Mail(app)
