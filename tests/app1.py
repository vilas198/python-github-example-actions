"""Flask app for cicd testing"""
from flask import Flask

APP = Flask(__name__)


@APP.route("/")
def index1():
    """Flask function for cicd testing"""
    return "Hello World"

if __name__ == "__main__":
    APP.run()
