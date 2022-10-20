from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, FieldList, FormField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length


class ColorInfo(FlaskForm):
    power = StringField(render_kw={"placeholder": "Puiss."})
    speed = StringField(render_kw={"placeholder": "Vit."})
    ppi = StringField()
    offset = StringField()
    focus = StringField()
    gravure = BooleanField()
    decoupe = BooleanField()
    airblow = BooleanField(render_kw={"label": "Ok"})


class LTTForm(FlaskForm):
    colorinfos = FieldList(FormField(ColorInfo), min_entries=8, max_entries=8)



