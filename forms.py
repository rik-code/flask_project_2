from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired


class StudentForm(FlaskForm):
    name = StringField('Student\'s name: ',
                       validators=[DataRequired()])
    birth_date = DateField('Birth date: ',
                           validators=[DataRequired()])

    mark = FloatField('Mark: ')
    subject = SubmitField('Subject', choices=[])
    status = SelectField('Learning status',
                         choices=[
                             ('free', 'Free'),
                             ('pay', 'Paid')
                         ])
    submit = SubmitField('Add')


class SubjectForm(FlaskForm):
    name = StringField('Subject\'s name: ',
                       validators=[DataRequired()])
    submit = SubmitField('Add')