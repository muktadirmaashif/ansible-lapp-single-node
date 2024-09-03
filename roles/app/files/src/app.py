from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    hello = """
    Hi from flask!
    """
    return hello
