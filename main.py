import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

GENDER = "male"
weight_kg = "84"
height_cm = "179"
AGE = "22"
today = datetime.today()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")
print(today)
print(time)

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_API_KEY = os.getenv("SHEETY_API_KEY")
print(SHEETY_API_KEY, API_KEY, APP_ID)

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/a08309ecbf8036ba1aa39f7cc7bae46e/copyOfMyWorkouts/workouts"

exercise_text = input("Tell me what exercises you did \n")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json",
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

print(result["exercises"][0]["name"])

for exercise in result["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
sheety_headers = {
    "Authorization": f"Bearer {SHEETY_API_KEY}"
}
sheety_response = requests.post(sheety_endpoint, json=sheety_parameters, headers=sheety_headers)
print(sheety_response.json())