from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateField
from wtforms.validators import DataRequired

class ActivityForm(FlaskForm):
    activity = StringField('activity', validators=[DataRequired()])
    creatorId = IntegerField('creatorId', validators=[DataRequired()])
