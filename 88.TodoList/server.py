from flask import Flask, render_template, redirect, url_for, flash, abort, request
from flask_bootstrap import Bootstrap
from datetime import date
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, URL
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from wtforms import StringField, SubmitField, PasswordField
import smtplib
from flask import url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# Cafe TABLE Configuration


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    admin = db.Column(db.Boolean, nullable=False)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


# Form Cafe


class CafeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    map_url = StringField('Map URL', validators=[DataRequired(), URL()])
    img_url = StringField('Image URL', validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    seats = StringField('Seats', validators=[DataRequired()])
    has_toilet = BooleanField('Has Toilet')
    has_wifi = BooleanField('Has WiFi')
    has_sockets = BooleanField('Has Sockets')
    can_take_calls = BooleanField('Can Take Calls')
    coffee_price = StringField('Coffee Price')
    submit = SubmitField("Validate")


@app.route('/')
def home():
    all_cafe = Cafe.query.all()
    return render_template("index.html", all_cafe=all_cafe)


@app.route("/add", methods=['GET', 'POST'])
def post_new_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)


@app.route("/reported/<cafe_id>")
def delete_cafe(cafe_id):
    the_cafe = Cafe.query.get(cafe_id)
    # my_email = ""
    # password = ""
    # # Connect to the SMTP server using a secure connection
    # smtp_server = "smtp.gmail.com"
    # smtp_port = 587
    # connection = smtplib.SMTP(smtp_server, smtp_port)
    # connection.starttls()
    # # Login
    # connection.login(user=my_email, password=password)
    # test email

    message = (
        f"Cafe Reported ! \n {cafe_id}\n{the_cafe.name}\nreported Closed !")
    print(message)
    # connection.sendmail(from_addr=my_email,
    #                     to_addrs=my_email, msg=f"{message}")
    # connection.quit()

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
