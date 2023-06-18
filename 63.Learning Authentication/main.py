from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'files')

db = SQLAlchemy(app)
login_manager = LoginManager(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if User.query.filter_by(email=request.form.get('email')).first():
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        hashed_password = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)

        new_user = User(email=request.form.get("email"), password=hashed_password,
                        name=request.form.get("name"))
        db.session.add(new_user)
        db.session.commit()
        # Log in and authenticate user after adding details to database.
        login_user(new_user)
        return render_template("secrets.html", user=new_user, logged_in=current_user.is_authenticated)
    return render_template("register.html")


@login_manager.user_loader
def load_user(email):
    user = db.session.query(User).filter_by(email=email).first()
    return user


def let_him_in(email, password):
    user = load_user(email)
    if user:
        password_real = user.password
        password_same = check_password_hash(password_real, password)
        if password_same:
            return True
    return False


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mail = request.form.get("email")
        password = request.form.get("password")
        if let_him_in(mail, password):
            user = load_user(mail)
            login_user(user)
            return render_template("secrets.html", user=user, logged_in=current_user.is_authenticated)
        else:
            flash("Invalid email or password")
        return render_template("login.html")
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    filename = "cheat_sheet.pdf"
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == "__main__":
    app.run(debug=True)
