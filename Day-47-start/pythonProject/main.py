from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


response = requests.get(url="https://appbrewery.github.io/instant_pot/")
soup = BeautifulSoup(response.text, "html.parser")
Electric_pressure_price = soup.find(name="span", class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay")
x = Electric_pressure_price.text.split("$")[1]
print(x)

#