from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "YOOO WHAT IS UP MY DAWGSSSSSSS\n" \
           "WE BOUTA BE LIT"