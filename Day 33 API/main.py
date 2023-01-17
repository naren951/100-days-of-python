import time
import requests
from datetime import datetime
import smtplib
from dotenv import dotenv_values

config = dotenv_values(".env")

MY_LAT = 12.969972  # Your latitude
MY_LONG = 77.680679  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
def send_mail(message, mail):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        my_email = config["EMAIL"]
        password = config["PASSWORD"]
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=mail,
            msg=message,
        )


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(120)
    if abs(MY_LAT - iss_latitude) == 5 and abs(MY_LONG - iss_latitude) == 5:
        if time_now.hour > sunset or time_now.hour < sunrise:
            send_mail(
                message="Subject:Look Up\n\nISS is overhead",
                mail=config["EMAIL"],
            )
