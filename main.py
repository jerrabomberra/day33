import requests
from datetime import datetime
import smtplib
import haversine as hs


MY_LAT = -38.373955
MY_LNG = 144.918053
MY_TIMEZ = "Australia/Melbourne"
FORMATTED = 0


MY_EMAIL = "jerrabomberra@gmail.com"
MY_PASSWORD = "bxettybczgryheag"


# SEND EMAILS
def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="gordononline@bigpond.com",
            msg=f"Subject:ISS is overhead!\n\nThe international space station is currently overhead at {iss_latitude}, {iss_longitude}",
        )


# send_email()

# get iss location now
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "tzid": MY_TIMEZ,
    "formatted": FORMATTED,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

loc1 = (iss_latitude, iss_longitude)
loc2 = (MY_LAT, MY_LNG)
distance = round(hs.haversine(loc1, loc2), 2)
print(f"The Iss is {distance} km away from your location")

if (
    abs(iss_latitude - MY_LAT) <= 5
    and abs(iss_longitude - MY_LNG) <= 5
    and not (sunrise < time_now < sunset)
):
    send_email()
    print("I'm here")
# Your position is within +5 or -5 degrees of the ISS position.
# get sunrise and sunset to determine if it should be dark now
