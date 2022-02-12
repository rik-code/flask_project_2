from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired


class StudentForm(FlaskForm):
    name = StringField('Student\'s name: ',
                       validators=[DataRequired()])
    birth_date = DateField('Birth date: ',
                           validators=[DataRequired()])
    mark = FloatField('Mark: ')
    # TODO: SelectMultipleField for subject_id field
    status = StringField('')
