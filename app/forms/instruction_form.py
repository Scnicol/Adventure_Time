from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired

class InstructionForm(FlaskForm):
    instructions = StringField('instructions', validators=[DataRequired()])
    adventureId = IntegerField('adventureId', validators=[DataRequired()])
