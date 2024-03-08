from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateField
from wtforms.validators import DataRequired

class DirectionForm(FlaskForm):
    direction = StringField('direction', validators=[DataRequired()])
    creatorId = IntegerField('creatorId', validators=[DataRequired()])
