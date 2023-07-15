import requests
from datetime import datetime


my_lat = -33.966309
my_long = 151.101273

parameters = {
    "lat": my_lat,
    "log": my_long,
    "formatted": 0

}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now)