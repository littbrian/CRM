from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Employee

class RegistrationForm(FlaskForm):
    #form for users to create new accounts

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField("First Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[
        DataRequired(),
        EqualTo('confirm_password', message='Passwords must match')
    ])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self,field):
        if Employee.query.filter_by(email=field.data).first():
            raise ValidationError("Email is already in use.")

    def validate_username(self,field):
        if Employee.query.filter_by(username=field.data).first():
            raise ValidationError("Username is already in use.")
    
    
class LoginForm(FlaskForm):
    #form for users to login
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')