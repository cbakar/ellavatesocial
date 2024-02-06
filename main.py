import os
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(error):
    path = request.path
    return render_template("404.html", path=path), 404


if __name__ == "__main__":
    app.run(debug=False)
