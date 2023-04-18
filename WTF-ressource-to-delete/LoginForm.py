from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField('Mail', validators=[DataRequired(), Email(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=80)])
    submit = SubmitField(label="Log In")
