import smtplib
import datetime as dt
import random
from dotenv import load_dotenv

config = load_dotenv(".env")


def send_mail(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        my_email = config.EMAIL
        password = config.PASSWORD
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="narendiran.work@gmail.com",
            msg=f"Subject:Test\n\nTesting {message}",
        )


if dt.datetime.now().weekday() == 5:
    with open("quotes.txt") as file:
        quotes = file.readlines()
    send_mail(random.choice(quotes))
