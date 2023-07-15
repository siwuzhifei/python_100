import requests

HV_latitude = -33.968109
HV_longitude = 151.104080


my_parameters = {
    "lat": HV_latitude,
    "log": HV_longitude,
    "exclude": "hourly, daily",
    "appid": "ca298b529aa985431f05b0154c68649f",
    "formatted": 0

}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=my_parameters)
response.raise_for_status()
data = response.json()

sunrise = data["current"]["sunrise"]
print(sunrise)