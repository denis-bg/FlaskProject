import os

from flask import render_template, flash, redirect, url_for, request, send_from_directory
from werkzeug.utils import secure_filename
from app import app, lttdir, fichiers
from app.forms import LTTForm, UploadForm
from collections import namedtuple


def populateLTTForm(filename):
    def divby10(s):
        l = len(s) - 1
        return s[:l] + '.' + s[l:]

    path = app.root_path + '/public/lttfiles/'
    file = path + filename
    with open(file, 'r') as f:
        list = [line.rstrip('\n') for line in f]

    premiere_ligne = list.pop(0)
    lttinfos = dict(kv.split('=') for kv in list)

    pow = lttinfos['Power'].split(" ")
    spe = lttinfos['Speed'].split(" ")
    ppi = lttinfos['PPI'].split(" ")
    foc = lttinfos['ZaxisOffset'].split(" ")
    off = lttinfos['PolygonOffset'].split(" ")
    gra = lttinfos['EngraveFlag'].split(" ")
    dec = lttinfos['CutFlag'].split(" ")
    air = lttinfos['AirBlowFlag'].split(" ")

    colorinfo = namedtuple('ColorInfo', ['power', 'speed', 'ppi', 'offset', 'focus', 'gravure', 'decoupe', 'airblow'])
    ci = []
    for i in range(8):
        ci.append(colorinfo(divby10(pow[i]), divby10(spe[i]), ppi[i], off[i], foc[i], 0 if '0' in gra[i] else 1,
                            0 if '0' in dec[i] else 1, 0 if '0' in air[i] else 1))

    print(0 if '0' in gra else 1)
    data = {
        'colorinfos': ci,
        'chkgravure': 0 if '0' in gra else 1,
        'chkdecoupe': 0 if '0' in dec else 1,
        'chkairblow': 0 if '0' in air else 1,
    }
    return data


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/info')
def showdir():
    a = "root_path : %s" % app.instance_path
    return a


@app.route('/lttconfig', methods=['GET', 'POST'], strict_slashes=False)
@app.route('/lttconfig/<name>', methods=['GET', 'POST'], strict_slashes=False)
def lttconfig(name=None):
    if not name:
        filename = 'DEFAULT-LTT.LCF'
    else:
        filename = os.path.basename(name)
        print(name+'-'+filename)
    data = populateLTTForm(filename)
    # data = populateLTTForm('text.txt')

    form = LTTForm(data=data)
    if form.validate_on_submit():
        # A FAIRE : enregistrement du fichier
        flash('Fichier enregistré', 'danger')
        return render_template('ltt_config.html', form=form)
        '''
        print('debut')
        for ci in form.colorinfos:
            print(ci.power.data)
        print('fin')
        '''

    print(form.errors)
    return render_template('ltt_config.html', form=form)


@app.route('/newfile', methods=['GET', 'POST'])
def newfile():
    data = populateLTTForm('DEFAULT-LTT.LCF')
    # data = populateLTTForm('text.txt')

    form = LTTForm(data=data)
    if form.validate_on_submit():
        # A FAIRE : enregistrement du fichier
        flash('Fichier enregistré', 'danger')
        return render_template('ltt_config.html', form=form)
        '''
        print('debut')
        for ci in form.colorinfos:
            print(ci.power.data)
        print('fin')
        '''

    print(form.errors)
    return render_template('ltt_config.html', form=form)


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'file' in request.files:
        fichiers.save(request.files['file'])
        flash("Fichier saved successfully.")
        # return render_template('upload.html')
        return redirect(url_for('lttconfig', name=request.files['file'].filename))
        # return request.files['file'].filename
    return render_template('upload.html')


@app.route('/nup', methods=['GET', 'POST'])
def nup():
# https://n8henrie.com/2015/05/better-bootstrap-file-upload-button/
# A CORRIGER
    form = UploadForm()
    if request.method == 'POST' and form.validate_on_submit():
        input_file = request.files['input_file']
        fichiers.save(input_file)
        return redirect(url_for('lttconfig', name=input_file.filename))
        # Do stuff
    else:
        return render_template('nupload.html', form=form)

@app.route('/wfile')
def writefile():
    path = app.root_path + '/public/lttfiles/'
    file = path + 'montest.txt'
    fo = open(file, "w")
    filebuffer = ["brave new world"]
    fo.writelines(filebuffer)
    fo.close()
    return 'ok'

'''
@app.route('/showltt', methods=['GET', 'POST'])
def showltt():
    colorinfo = namedtuple('ColorInfo', ['power', 'speed', 'ppi', 'offset', 'focus'])
    data = {
        'colorinfos': [
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
    # return render_template('testpane.html', form=form)
    return render_template('ltt_config.html', form=form)
'''



