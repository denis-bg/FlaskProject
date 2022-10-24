from flask_wtf import FlaskForm, Form

from wtforms import DecimalField, StringField, FieldList, FormField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length


class GDAInfo(FlaskForm):
    gravure = BooleanField(label="")
    decoupe = BooleanField(label="")
    airblow = BooleanField(label="")


class ColorInfo(Form):
    # power = StringField(render_kw={"placeholder": "Puiss."})
    power = StringField()
    speed = StringField()
    ppi = StringField()
    offset = StringField()
    focus = StringField()
    gravure = BooleanField(label="G")
    decoupe = BooleanField(label="D")
    airblow = BooleanField(label="A")


class LTTForm(FlaskForm):
    colorinfos = FieldList(FormField(ColorInfo), min_entries=8, max_entries=8)
    chkgravure = BooleanField(label="G")
    chkdecoupe = BooleanField(label="D")
    chkairblow = BooleanField(label="A")



