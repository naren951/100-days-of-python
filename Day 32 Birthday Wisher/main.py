##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import pandas as pd
import smtplib
import datetime as dt
from dotenv import dotenv_values

config = dotenv_values(".env")
birthdays = pd.read_csv("birthdays.csv")


def send_mail(message, mail):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        my_email = config["EMAIL"]
        password = config["PASSWORD"]
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=mail,
            msg=f"Subject:Happy Birthday\n\n{message}",
        )


for _, row in birthdays.iterrows():
    today = dt.datetime.now()
    if row["day"] == today.day and row["month"] == today.month:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
            message = file.read()
            message = message.replace("[NAME]", row["name"])
            send_mail(message=message, mail=row["email"])
