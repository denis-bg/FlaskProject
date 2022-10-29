from flask_wtf import FlaskForm, Form
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import DecimalField, StringField, FieldList, FormField, BooleanField, FileField, SubmitField, RadioField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length


class UploadForm(Form):

    validators = [
        FileRequired(message='There was no file!'),
        FileAllowed(['lcf, LCF'], message='Must be a LCF file!')
    ]

    input_file = FileField('', validators=validators)
    submit = SubmitField(label="Upload")


class GDAInfo(FlaskForm):
    gravure = BooleanField(label="")
    decoupe = BooleanField(label="")
    airblow = BooleanField(label="")


class ColorInfo(Form):
    # power = StringField(render_kw={"placeholder": "Puiss."})
    power = StringField(validators=[DataRequired()])
    speed = StringField(validators=[DataRequired()])
    ppi = StringField(validators=[DataRequired()])
    offset = StringField(validators=[DataRequired()])
    focus = StringField(validators=[DataRequired()])
    gravure = BooleanField(label="")
    decoupe = BooleanField(label="")
    airblow = BooleanField(label="")


class LTTForm(FlaskForm):
    colorinfos = FieldList(FormField(ColorInfo), min_entries=8, max_entries=8)
    # chkgravure = BooleanField(label="Gravure")
    # chkdecoupe = BooleanField(label="Découpe")
    # chkairblow = BooleanField(label="Airblow")
    trvgravure   = BooleanField(label="Gravure")
    trvdecoupe   = BooleanField(label="Découpe")
    trvairblow   = BooleanField(label="Airblow")
    trvmode      = RadioField('', choices=[('0','Normal'),('1','Tampon'),('2','Gris (3D)')])
    trvtrame     = BooleanField('Trame')
    trv16niv     = BooleanField('16 niveaux')
    trvmethode   = SelectField('Méthode', choices=[('0', 'Méthode 1'), ('1', 'Méthode 2'), ('2', 'Méthode 3'),
                                                  ('3', 'Méthode 4'), ('4', 'Méthode 5'), ('5', 'Méthode 6')])
    trvresol    = SelectField('Résolution', choices=[('0', '1000'), ('1', '800'), ('2', '666'), ('3', '500'),
                                                     ('4',  '333'), ('5', '250'), ('6', '200'), ('7', '166')])
    trvoffset   = StringField('Offset')
    trvtypemode = SelectField('Mode', choices=[('0', 'Normal'), ('1', 'Précis')])
    trvtypedir  = SelectField('Direction', choices=[('0', 'Haut vers Bas'), ('1', 'Bas vers Haut')])
    trvpulsecpt = StringField('Compteur')
    trvpulseon  = StringField('Période')
    trvpulseoff = StringField('Pause Période')
    trvmodenb   = BooleanField('N&B')
    trvoptimvect = BooleanField('Optim. Vect.')
    trvmirror    = BooleanField('Mirroir')
    trvjctcurve  = BooleanField('Jct courbes')
    trvpulse     = BooleanField('Impulsion')
    trvnegatif   = BooleanField('Négatif')






