import requests
from pprint import pprint
from flight_search import FlightSearch
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

sheety_get_url = "https://api.sheety.co/ad16d8e01eedaf21de03cc58acac0066/flightSerch/prices"

response = requests.get(url=sheety_get_url)
result = response.json()
sheet_data = result['prices']
pprint(sheet_data)
