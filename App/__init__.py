from flask import Flask
from flask_sqlalchemy import SQLAlchemy




# Initialize the Flask application
app = Flask(__name__)
# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/market.db'
app.config['SECRET_KEY'] = '008df3592c3dd620aed90ea7'
# creating the database file in the instance folder
db = SQLAlchemy(app)
from App import routes  # Import routes to register them with the app