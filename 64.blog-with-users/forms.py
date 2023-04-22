from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Regexp
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

class CreateContactForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    email_address = StringField("Email address: ", validators=[DataRequired(), Email()])
    number = StringField("Phone Number : ", validators=[DataRequired(), Regexp('^(\d{2})\s(\d{2})\s(\d{2})\s(\d{'
                                                                               '2})\s(\d{2})$', message='Phone number '
                                                                                                        'must be in '
                                                                                                        'the format '
                                                                                                        'of XX XX XX '
                                                                                                        'XX XX')])
    message = StringField("Message: ", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
