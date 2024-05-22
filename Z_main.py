import requests
from datetime import datetime


MY_LAT = -38.373955
MY_LNG = 144.918053
MY_TIMEZ = "Australia/Melbourne"
FORMATTED = 0


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "tzid": MY_TIMEZ,
    "formatted": FORMATTED,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
rise = data["results"]["sunrise"].split("T")[1].split(":")[0]
set = data["results"]["sunset"].split("T")[1].split(":")[0]

print(rise, set)

print(datetime.now().hour)
