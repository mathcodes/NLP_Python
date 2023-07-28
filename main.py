import requests

url = 'https://trackapi.nutritionix.com/v2/locations'
headers = {
    'x-app-id': '7a0b8d53',
    'x-app-key': 'c9b14420b1ed4b976339e22638f8da52'
}
params = {
    'll': '38.89814,-77.029446',
    'distance': '50m',
    'limit': '1'
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)