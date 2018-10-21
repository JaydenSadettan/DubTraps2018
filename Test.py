from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "DubTraps 2018 PLEASE WORK "
