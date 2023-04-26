import os
import smtplib
import requests as requests
from dotenv import load_dotenv
from flask import Flask, render_template, flash, request

dotenv_path = ".env.txt"
load_dotenv(dotenv_path)


app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")
response = requests.get('https://api.npoint.io/769606a80bbde3ea751f')
all_projects = response.json()
SECRET_KEY = os.getenv("SECRET_KEY")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")


@app.route('/')
def home():
    return render_template("index.html")


def send_mail(nom, mail, numero, message):
    # Connect to the SMTP server using a secure connection
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    connection = smtplib.SMTP(smtp_server, smtp_port)
    connection.starttls()
    # Login
    print(MY_EMAIL)
    print(MY_PASSWORD)

    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    # test email
    message = f"New Message\nNom : {nom}\nmail : {mail}\nNumero : {numero}\n Message : {message}"
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"{message}")
    connection.quit()


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        if data["name"] and data["email"] and data["message"] != "":
            send_mail((data["name"]),
                      (data["email"]),
                      (data["phone"]),
                      (data["message"]))
            return render_template("contact.html", msg_sent=True)
        else:
            flash("You can't send a message without filling name, email and message fields.")
            return render_template("contact.html", msg_sent=False)
    else:
        return render_template("contact.html", msg_sent=False)


@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    # form = CreateContactForm()
    return render_template("portfolio.html", all_projects=all_projects)


if __name__ == "__main__":
    app.run(debug=True)
