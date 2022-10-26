from flask_wtf import FlaskForm, Form

from wtforms import DecimalField, StringField, FieldList, FormField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length


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



