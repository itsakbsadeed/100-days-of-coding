import requests

MY_LAT = 53.480709
MY_LONG = -2.234380
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
#
# data = response.json()["timestamp"]
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lag": MY_LAT,
    "lng": MY_LONG,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
