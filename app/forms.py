from flask_wtf import FlaskForm, Form
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import DecimalField, StringField, FieldList, FormField, BooleanField, FileField, SubmitField
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
    chkgravure = BooleanField(label="")
    chkdecoupe = BooleanField(label="")
    chkairblow = BooleanField(label="")



