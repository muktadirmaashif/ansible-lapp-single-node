from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

app = Flask(__name__)
# Configure your database URI here
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lamp:lamp_password@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    hello = """
    Hi from flask!
    """
    return hello

@app.route('/test_db')
def test_db_connection():
    try:
        # Attempt to execute a simple query
        db.session.execute(text('SELECT 1'))
        return 'Database connection successful!'
    except SQLAlchemyError as e:
        # If there's an error, return the error message
        return f'Database connection failed: {str(e)}'

