import requests


MY_LAT = -38.373955
MY_LNG = 144.918053
MY_TIMEZ = "Australia/Melbourne"


parameters = {"lat": MY_LAT, "lng": MY_LNG, "tzid": MY_TIMEZ}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
rise = data["results"]["sunrise"]
set = data["results"]["sunset"]
print(rise, set)
