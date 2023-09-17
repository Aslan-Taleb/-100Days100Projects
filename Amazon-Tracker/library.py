import re
import smtplib
import requests
from bs4 import BeautifulSoup

# HERE
LINK = "https://www.amazon.fr/METAL-BOXE-Jeunesse-unisexe-Junior/dp/B09ZJDZXS4/ref=sr_1_5?crid=3RWU9WV5URYUT&keywords=gant+de+boxe&qid=1694961903&sprefix=gang%2Caps%2C169&sr=8-5"
PRICE_WANTED = 0


def get_amazon_page(link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6",
    }
    try:
        response = requests.get(link, headers=headers)
    except requests.exceptions.MissingSchema:
        html = ""
    else:
        html = response.text
    return html


def get_information(html):
    soup = BeautifulSoup(html, "html.parser")
    product_title = soup.find(id="productTitle")
    price = soup.find(class_="a-price-whole")
    virgule = soup.find(class_="a-price-fraction")

    price = price.getText()
    virgule = virgule.getText()
    product_title = product_title.getText().replace(" ", "")
    product = [product_title, price, virgule]
    return product


def send_mail(message):
    my_email = "aslantalebselim@gmail.com"
    password = "tu_pense"

    # Connect to the SMTP server using a secure connection
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    connection = smtplib.SMTP(smtp_server, smtp_port)
    connection.starttls()

    # Login
    connection.login(user=my_email, password=password)

    # Send email
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Amazon Price Alert 😱\n\n{message}")
    connection.quit()

    print(f"Sent message:\n{message}\n\nTo email address: {my_email}\n")


def i_send_or_not(product, price_wanted):
    message = None
    the_price = float(product[1] + product[2])
    limited_string = product[0][:25]
    print(f"Searching for the price {price_wanted} for your product: {limited_string}...")
    if the_price <= price_wanted:
        message = f"Your product: {limited_string} is now available for {the_price}\nLink: {LINK}"
    else:
        print("The price is too high.\n")
    return message
