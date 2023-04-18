from LoginForm import *

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'my_secret_key'
email_admin = "admin@email.com"
password_admin = "12345678"


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data
        if email == email_admin and password == password_admin:
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
