import smtplib

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

response = requests.get('https://api.npoint.io/db04ea0124698e4ff18c')
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        mail = request.form['email']
        phone = request.form['phone']
        return send_mail(mail, message, phone, name)
    else:
        return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/<id_post>')
def post(id_post):
    post_to_show = all_posts[int(id_post) - 1]
    title = post_to_show['title']
    body = post_to_show['body']
    subtitle = post_to_show['subtitle']
    image = post_to_show['post_image']
    return render_template("post.html", the_post=post_to_show, title=title, body=body,
                           subtitle=subtitle,
                           image=image)


def send_mail(mail, message, numero, nom):
    # my_email = "aslantalebselim@gmail.com"
    # password = "***"
    # # Connect to the SMTP server using a secure connection
    # smtp_server = "smtp.gmail.com"
    # smtp_port = 587
    # connection = smtplib.SMTP(smtp_server, smtp_port)
    # connection.starttls()
    # # Login
    # connection.login(user=my_email, password=password)
    # test email
    message = f"New Message Blog\nNom : {nom}\nmail : {mail}\nNumero : {numero}\n Message : {message}"
    # connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=message)
    # connection.quit()
    print(message)
    return render_template("contact.html", msg_sent=True)


if __name__ == "__main__":
    app.run(debug=True)
