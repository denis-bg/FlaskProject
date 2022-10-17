from flask import Flask

app = Flask(__name__)


from app.routes import *


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
