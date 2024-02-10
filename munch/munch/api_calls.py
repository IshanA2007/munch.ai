import base64
import requests
import json
import settings
base_dir = settings.BASE_DIR

api_key = "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"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "/munch/thonger.png"
real_image_path = str(base_dir) + image_path



def read_image(image_path):
    # Getting the base64 string
    base64_image = encode_image(image_path)
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Output the text in this image. Do NOT output anything else."
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    return response.json()['choices'][0]['message']['content']

def calc_macros(food):
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {
        "Content-Type": "application/json",
        "x-app-id": "4a0a944f",
        "x-app-key": "adb35788f38d5d1c39b79ceaf560497f",
    }
    data = {"query": food}

    response = requests.post(url, headers=headers, data=json.dumps(data))
    calories = 0
    protein = 0
    carbs = 0
    fats = 0
    for food in response.json()["foods"]:
        print(food)
        calories += food["nf_calories"]
        protein += food["nf_protein"]
        carbs += food["nf_total_carbohydrate"]
        fats += food["nf_total_fat"]
    return {"Calories": calories, "Protein": protein, "Carbs": carbs, "Fat": fats}

def image_to_info(image_path):
   return calc_macros(read_image(image_path))