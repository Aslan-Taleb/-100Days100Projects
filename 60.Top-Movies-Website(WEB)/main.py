from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import CheckConstraint, Column, String
from wtforms import StringField, SubmitField, DecimalField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)
API_KEY = "c82c4a923ca7725a8f6a8dd64891fff8"

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(
        String(4), CheckConstraint("year BETWEEN 1900 AND 2100"), nullable=False
    )
    description = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float(), nullable=False)
    ranking = db.Column(db.Integer(), nullable=False, unique=True)
    review = db.Column(db.String(250), unique=False, nullable=False)
    img_url = db.Column(db.String(1000), unique=False, nullable=False)

    # with app.app_context():
    #   db.create_all()


class UpdateForm(FlaskForm):
    rating = DecimalField("Rating (out of 10)", validators=[DataRequired()])
    review = TextAreaField("Your Review", validators=[DataRequired(), Length(max=500)])
    submit = SubmitField(label="Update Rating and Review")


class AddMovieForm(FlaskForm):
    Title = TextAreaField("Title", validators=[DataRequired(), Length(max=25)])
    submit = SubmitField(label="Search Movie")


@app.route("/")
@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = UpdateForm()
    id_to_change = request.args.get("id")
    movie_to_update = Movie.query.filter_by(id=id_to_change).first()
    if form.validate_on_submit():
        new_rating = request.form["rating"]
        new_review = request.form["review"]
        movie_to_update.rating = new_rating
        movie_to_update.review = new_review
        return home()
    return render_template("edit.html", movie_to_change=movie_to_update, form=form)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    id_delete = request.args.get("id")
    movie_to_delete = Movie.query.get(id_delete)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return home()


def get_movie(title):
    movies = []
    link = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"
    response = requests.get(link)
    response = response.json()["results"]
    for movie in response:
        movie_data = {
            "title": movie["title"],
            "year": movie["release_date"][:4],
            "id": movie["id"],
        }
        movies.append(movie_data)
    return movies


@app.route("/add", methods=["GET", "POST"])
@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = request.form["Title"]
        movies = get_movie(title)
        return render_template("select.html", movies=movies)
    else:
        return render_template("add.html", form=form)


@app.route("/choose", methods=["GET", "POST"])
def choose():
    movie_id = request.args.get("id")
    link = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(link)
    movie_data = response.json()
    new_movie = Movie(
        title=movie_data["title"],
        year=movie_data["release_date"][:4],
        description=movie_data["overview"],
        rating=0,
        ranking=0,
        review="",
        img_url=f"https://image.tmdb.org/t/p/w500/{movie_data['poster_path']}",
    )
    db.session.add(new_movie)
    db.session.commit()
    movie_to_update = Movie.query.filter_by(title=movie_data["title"]).first()
    return redirect(url_for("edit", id=movie_to_update.id))


if __name__ == "__main__":
    app.run(debug=True)
