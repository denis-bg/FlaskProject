import os

from flask import render_template, flash, redirect, url_for, request, send_from_directory
from werkzeug.utils import secure_filename
from app import app, lttdir, fichiers
from app.forms import LTTForm, UploadForm
from collections import namedtuple


def populateLTTForm(filename):
    def str2bool(s):
        return True if s == '1' else False

    def divby10pi(s, i):
        l = len(s) - i
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
        ci.append(colorinfo(divby10pi(pow[i], 1), divby10pi(spe[i], 1), ppi[i], off[i], foc[i],
                            0 if '0' in gra[i] else 1,
                            0 if '0' in dec[i] else 1,
                            0 if '0' in air[i] else 1))

    print(0 if '0' in gra else 1)
    data = {
        'colorinfos': ci,
        'chkgravure': 0 if '0' in gra else 1,
        'chkdecoupe': 0 if '0' in dec else 1,
        'chkairblow': 0 if '0' in air else 1,
        'trvmode': lttinfos['Mode'],
        'trvtrame': str2bool(lttinfos['Halftone']),
        'trv16niv': str2bool(lttinfos['CustomPower']),
        'trvmethode': lttinfos['DitheringMethod'],
        'trvresol': lttinfos['Resolution'],
        'trvoffset': lttinfos['StampOffset'],
        'trvtypemode': lttinfos['RasterEnd'],
        'trvtypedir': lttinfos['ScanlineOrder'],
        'trvpulsecpt': lttinfos['PulseCount'],
        'trvpulseon': divby10pi(lttinfos['PulseEnableTime'], 2),
        'trvpulseoff': divby10pi(lttinfos['PulseDisableTime'], 2),
        'trvmodenb': str2bool(lttinfos['GrayMode']),
        'trvoptimvec': str2bool(lttinfos['VectorOptimization']),
        'trvmirror': str2bool(lttinfos['Mirror']),
        'trvjctcurve': str2bool(lttinfos['JointCurves']),
        'trvpulse': str2bool(lttinfos['PulseMode']),
        'trvnegatif': str2bool(lttinfos['Invert']),

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
        print(name + '-' + filename)
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
