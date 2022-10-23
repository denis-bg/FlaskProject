from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, FieldList, FormField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length


class GDAInfo(FlaskForm):
    gravure = BooleanField(label="")
    decoupe = BooleanField(label="")
    airblow = BooleanField(label="")


class ColorInfo(FlaskForm):
    power = StringField(render_kw={"placeholder": "Puiss."})
    speed = StringField(render_kw={"placeholder": "Vit."})
    ppi = StringField()
    offset = StringField()
    focus = StringField()
    gravure = BooleanField(label="")
    decoupe = BooleanField(label="D")
    airblow = BooleanField(label="A")


class LTTForm(FlaskForm):
    colorinfos = FieldList(FormField(ColorInfo), min_entries=8, max_entries=8)



