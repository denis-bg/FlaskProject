from flask import render_template, flash, redirect, url_for, request
from app import app


@app.route('/showltt')
def showltt():
    return render_template('showltt.html')


@app.route("/")
def home():
    return render_template("home.html")

