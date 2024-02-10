import requests
import json
food = input("enter stuff:")
food = "1/2 a pound of grilled chicken, 2 oreos (mint), and 1/3 of an orange (peeled)"
url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
headers = {
    'Content-Type': 'application/json',
    'x-app-id': '4a0a944f',
    'x-app-key': 'adb35788f38d5d1c39b79ceaf560497f'
}
data = {
    'query': food
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(type(response))

# Print the status code and returned data
print('Returned Data:', response.json())
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaa")
print(type(response.json()['foods'][0]))
print(len(response.json()['foods'][0]))
print("stuff in foods[0]:")
calories = 0
protein = 0
carbs = 0
fats = 0
for food in response.json()['foods']:
    calories += food['nf_calories']
    protein += food['nf_protein']
    carbs += food['nf_total_carbohydrate']
    fats += food['nf_total_fat']

print("total calories:", calories)
print("total protein:", protein)
print("total carbs:", carbs)
print("total fat:", fats)