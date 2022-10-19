from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, FieldList, FormField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length


class ColorInfo(FlaskForm):
    power = StringField()
    speed = StringField()
    ppi = StringField()
    offset = StringField()
    focus = StringField()


class LTTForm(FlaskForm):
    colorinfos = FieldList(FormField(ColorInfo), min_entries=8, max_entries=8)


class NOKLTTForm(FlaskForm):
    power_0 = StringField()
    speed_0 = StringField()
    ppi_0 = StringField()
    offset_0 = DecimalField(places=2, validators=[])
    focus_0 = DecimalField(places=2, validators=[])

    power_1 = DecimalField(places=2, validators=[])
    speed_1 = DecimalField(places=2, validators=[])
    ppi_1 = DecimalField(places=2, validators=[])
    offset_1 = DecimalField(places=2, validators=[])
    focus_1 = DecimalField(places=2, validators=[])

    power_2 = DecimalField(places=2, validators=[])
    speed_2 = DecimalField(places=2, validators=[])
    ppi_2 = DecimalField(places=2, validators=[])
    offset_2 = DecimalField(places=2, validators=[])
    focus_2 = DecimalField(places=2, validators=[])

    power_3 = DecimalField(places=2, validators=[])
    speed_3 = DecimalField(places=2, validators=[])
    ppi_3 = DecimalField(places=2, validators=[])
    offset_3 = DecimalField(places=2, validators=[])
    focus_3 = DecimalField(places=2, validators=[])

