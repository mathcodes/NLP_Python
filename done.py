import requests

GENDER = 'male'
WEIGHT_KG = '200'
HEIGHT_CM = '150'
AGE = '41'

APP_ID = '7a0b8d53'
API_KEY = 'c9b14420b1ed4b976339e22638f8da52'

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)