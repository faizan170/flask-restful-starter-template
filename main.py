from config import app
from flask import request, render_template, jsonify

@app.route("/")
def main_route():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
