from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

# VERSION SQLALCHEMY
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
Bootstrap(app)
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# VERSION SQL


# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) "
#                "NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


@app.route('/', methods=['GET', 'POST'])
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get("title")
        author = request.form.get("author")
        rating = request.form.get("rating")
        book = Book(title=title, author=author, rating=rating)
        db.session.add(book)
        db.session.commit()
        all_books = db.session.query(Book).all()
        return render_template('index.html', books=all_books)
    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    id_to_change = request.args.get('id')
    book_to_update = Book.query.filter_by(id=id_to_change).first()
    if request.method == 'POST':
        new_rating = request.form['rating']
        book_to_update.rating = new_rating
        return home()
    print("test")
    return render_template('edit.html', book_to_change=book_to_update)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    id_delete = request.args.get('id')
    book_to_delete = Book.query.get(id_delete)
    db.session.delete(book_to_delete)
    db.session.commit()
    return home()


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
