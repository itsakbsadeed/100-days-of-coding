import requests
from datetime import datetime

GENDER = "Male"
WEIGHT_KG = "75"
HEIGHT_CM = "175"
AGE = "21"

APP_ID = "1ef65fcc"
API_KEY = "24ea139b4e3747b31f6f76d857fb6856"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/ad16d8e01eedaf21de03cc58acac0066/workoutTracking/hoja1"
exercise_text = input("Tell me what exercises you did:")

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}


response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "hoja1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs)
    print(sheet_response.text)