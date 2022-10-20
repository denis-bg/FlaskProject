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
            colorinfo(10.4, 90, '500', '0', '0'),
            colorinfo(100, 90.3, '500', '0', '0'),
            colorinfo(18.4, 37.2, '500', '0', '0'),
            colorinfo(65, 69, '500', '0', '0'),
        ]
    }
    form = LTTForm(data=data)
    if form.validate_on_submit():
        return 'Ok'
    # form.process()

    return render_template('showfields.html', form=form)




@app.route("/")
def home():
    return render_template("home.html")
