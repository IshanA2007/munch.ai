import requests
import json
def calc_macros(food):
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
    calories = 0
    protein = 0
    carbs = 0
    fats = 0
    for food in response.json()['foods']:
        calories += food['nf_calories']
        protein += food['nf_protein']
        carbs += food['nf_total_carbohydrate']
        fats += food['nf_total_fat']
    return {"Calories": calories, "Protein":protein, "Carbs":carbs, "Fat":fats}