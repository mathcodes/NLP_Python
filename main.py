import requests
import datetime
import os  # Import the 'os' module to use environment variables

GENDER = 'male'
WEIGHT_KG = '200'
HEIGHT_CM = '150'
AGE = '41'

APP_ID = '7a0b8d53'
API_KEY = 'c9b14420b1ed4b976339e22638f8da52'


# Alternatively, you can set the username and password as environment variables if you are using Basic Auth
os.environ["ENV_SHEETY_USERNAME"] = "root"
os.environ["ENV_SHEETY_PASSWORD"] = "root"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

# Nutritionix API Call
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
print(f"Nutritionix API call: \n {result} \n")

# Adding date and time
today_date = datetime.datetime.now().strftime("%d/%m/%Y")  # Use datetime.datetime.now()
now_time = datetime.datetime.now().strftime("%X")  # Use datetime.datetime.now()

# Sheety Project API. Check your Google sheet name and Sheety endpoint
# Sheety Project API. Check your Google sheet name and Sheety endpoint
# Correct the Sheety endpoint URL
sheet_endpoint = "https://api.sheety.co/1pvRELUorm5QZ037rj66hci7dkLDvAkzkE9oBYFIRdi8/sheetyData"

# Sheety Project API. Check your Google sheet name and Sheety endpoint
GOOGLE_SHEET_NAME = "sheet1"

# Correct the Sheety endpoint URL
sheet_endpoint = "https://api.sheety.co/aaae4f06011786880f4057df73fdc73a/sheetyData/sheet1"

# Sheety API Call & Authentication
for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Sheety Authentication Option 1: No Auth
    """
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    """

    # Sheety Authentication Option 2: Basic Auth
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            os.environ["ENV_SHEETY_USERNAME"],
            os.environ["ENV_SHEETY_PASSWORD"],
        )
    )

    # Sheety Authentication Option 3: Bearer Token
    """
    bearer_headers = {
        "Authorization": f"Bearer {os.environ['cm9vdDpyb290']}"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )    
    """
    pr
