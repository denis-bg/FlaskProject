from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LTTForm


@app.route('/showltt', methods=['GET', 'POST'])
def showltt():
    form = LTTForm()
    form.power_0.default = "54"
    form.speed_0.default = "85"
    if form.validate_on_submit():
        return 'Ok'
    # form.process()

    return render_template('show2.html', form=form)


@app.route("/")
def home():
    return render_template("home.html")
