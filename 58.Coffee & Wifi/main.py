import csv
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    rating_choices = [
        (1, '☕'),
        (2, '☕☕'),
        (3, '☕☕☕'),
        (4, '☕☕☕☕'),
        (5, '☕☕☕☕☕')
    ]
    wifi_choices = [
        (0, '❌'),
        (1, '💪'),
        (2, '💪💪'),
        (3, '💪💪💪'),
        (4, '💪💪💪💪'),
        (5, '💪💪💪💪💪')
    ]
    power_choices = [
        (0, '❌'),
        (1, '🔌'),
        (2, '🔌🔌'),
        (3, '🔌🔌🔌'),
        (4, '🔌🔌🔌🔌'),
        (5, '🔌🔌🔌🔌🔌')
    ]

    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location URL', validators=[DataRequired(), URL()])
    Open = StringField('Open', validators=[DataRequired()])
    Close = StringField('Close', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee rating', choices=rating_choices, coerce=int, validators=[DataRequired()])
    wifi_rating = SelectField('Wi-Fi rating', choices=wifi_choices, coerce=int, validators=[DataRequired()])
    power_rating = SelectField('Power outlet rating', choices=power_choices, coerce=int, validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        data = [
            form.cafe.data,
            form.location.data,
            form.Open.data,
            form.Close.data,
            '☕' * int(form.coffee_rating.data),
            '❌' if form.wifi_rating.data == 0 else '💪' * int(form.wifi_rating.data),
            '❌' if form.power_rating.data == 0 else '🔌' * int(form.power_rating.data)
        ]
        with open('cafe-data.csv', 'a', newline='\n', encoding='utf-8') as file:
            csv.writer(file).writerows([data])
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', 'r', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
