import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "8900374448ec140ea2f3c57c74f1afd2"

weather_params = {
    "lat": 53.480759,
    "lon": -2.242631,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)