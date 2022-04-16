from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField, SelectField, BooleanField, PasswordField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from models import User


class StudentForm(FlaskForm):
    name = StringField('Student\'s name: ',
                       validators=[DataRequired()])
    birth_date = DateField('Birth date: ',
                           validators=[DataRequired()])

    mark = FloatField('Mark: ')
    subject = SelectField('Subject', choices=[])
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


class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = StringField('Password:', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')


class RegisterForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    password_again = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email!')


class TeacherForm(FlaskForm):
    name = StringField('Teacher\'s name: ',
                       validators=[DataRequired()])
    subject = SelectField('Subject', choices=[])
    submit = SubmitField('Add')
