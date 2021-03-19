from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField, fields

class LoginForm(FlaskForm):
    email = StringField('email', [validators.DataRequired(), validators.Email(), validators.Length(max=100)])
    password = PasswordField('password', [validators.DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    email = StringField('Email Address', [validators.DataRequired(), validators.Email(), validators.Length(max=100)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Sign Up')