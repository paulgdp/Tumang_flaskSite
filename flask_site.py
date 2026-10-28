
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "Index page"

@app.route("/hello")
def hello():
    return "<h1>hi, world!</h1>"

@app.route("/hello/<user_name>")
def greet_user(user_name):
    return f"<h1>hi, {escape(user_name)}!</h1>"
