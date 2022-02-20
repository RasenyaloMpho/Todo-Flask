from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask("__main__")
Bootstrap(app) 

@app.route("/")
def index():
    return " Hello World!"