from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Herro Wolrd!"

@app.route("/about")
def about():
    return "About Me"