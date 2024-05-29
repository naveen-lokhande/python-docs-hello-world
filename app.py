from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello,i am naveen"

@app.route("/a")
def about():
    return "About Page"
