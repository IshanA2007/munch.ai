import requests
import json

url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
headers = {
    'Content-Type': 'application/json',
    'x-app-id': '4a0a944f',
    'x-app-key': 'adb35788f38d5d1c39b79ceaf560497f'
}
data = {
    'query': 'grape'
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# Print the status code and returned data
print('Status Code:', response.status_code)
print('Returned Data:', response.json())
