from flask import render_template, flash, redirect, url_for, request, send_from_directory
from app import app
from app.forms import LTTForm
from collections import namedtuple


@app.route('/testfile')
def showfile():
    return send_from_directory('public/lttfiles', "DEFAULT-LTT.LCF")
    # print(f.read())


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
        print('debut')
        for ci in form.colorinfos:
            print(ci.power.data)
        print('fin')

    # form.process()
    print(form.errors)
    return render_template('testpane.html', form=form)
    # return render_template('showltt.html', form=form)




@app.route("/")
def home():
    return render_template("home.html")
