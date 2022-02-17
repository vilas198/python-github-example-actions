"""Flask app for cicd testing"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Flask function for cicd testing"""
    return "Hello World fire"


if __name__ == "__main__":
    app.run()
