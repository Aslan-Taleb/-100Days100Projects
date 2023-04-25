from flask import Flask, render_template, redirect, url_for, flash, abort, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


def send_mail(mail, message, numero, nom):
    # form = CreateContactForm()
    # my_email = ""
    # password = ""
    # # Connect to the SMTP server using a secure connection
    # smtp_server = "smtp.gmail.com"
    # smtp_port = 587
    # connection = smtplib.SMTP(smtp_server, smtp_port)
    # connection.starttls()
    # # Login
    # connection.login(user=my_email, password=password)
    # # test email
    # message = f"New Message\nNom : {nom}\nmail : {mail}\nNumero : {numero}\n Message : {message}"
    # connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"{message}")
    # connection.quit()
    print(message)
    return render_template("contact.html", msg_sent=True)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # form = CreateContactForm()
    return render_template("contact.html")


@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    # form = CreateContactForm()
    return render_template("portfolio.html")


if __name__ == "__main__":
    app.run(debug=True)
