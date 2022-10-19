from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LTTForm
from collections import namedtuple


@app.route('/nokshowltt', methods=['GET', 'POST'])
def nonshowltt():
    form = LTTForm()
    form.power_0.default = "54"
    form.speed_0.default = "85"
    if form.validate_on_submit():
        return 'Ok'
    # form.process()

    return render_template('showltt.html', form=form)


@app.route('/showltt', methods=['GET', 'POST'])
def showltt():
    colorinfo = namedtuple('ColorInfo', ['power', 'speed', 'ppi', 'offset', 'focus'])
    data = {
        'colorinfos' : [
            colorinfo('10', '90', '500', '0', '0')
            colorinfo('20', '80', '500', '0', '0')
            colorinfo('30', '70', '500', '0', '0')
            colorinfo('40', '60', '500', '0', '0')
            colorinfo('50', '50', '500', '0', '0')
            colorinfo('60', '40', '500', '0', '0')
            colorinfo('70', '30', '500', '0', '0')
            colorinfo('80', '20', '500', '0', '0')
        ]
    }
    form = LTTForm()
    if form.validate_on_submit():
        return 'Ok'
    # form.process()

    return render_template('showltt.html', form=form)




@app.route("/")
def home():
    return render_template("home.html")
