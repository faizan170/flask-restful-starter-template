from config import app
from flask import requests, render_template, jsonify

@app.route("/")
def main_route():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()