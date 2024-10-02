from datetime import datetime
import requests
import os

GENDER = 'male'
WEIGHT_KG = 80
HEIGHT_CM = 184
AGE = 20

BASIC_AUTHORIZATION = os.environ.get("BASIC_AUTHORIZATION")
API_KEY = os.environ.get("API_KEY")
API_ID = os.environ.get("API_ID")

notrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}
user_input = input("Tell me which exercises you did: ")
parameters = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=notrition_endpoint, json=parameters, headers=headers)

headers = {
    "Authorization": BASIC_AUTHORIZATION
}
exercise_data = response.json()["exercises"]
now = datetime.now()
today_date = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime("%X")

# new_row ={'workout':{}}
for exercise in exercise_data:
    new_row = {
        "workout": {
            "date": today_date,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }
    response = requests.post(url=SHEET_ENDPOINT, json=new_row, headers=headers)
    print(response.text)
