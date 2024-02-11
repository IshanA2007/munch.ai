import base64
import requests
import json
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
import openai


# setting path
sys.path.append("../munch")

from munch import settings

base_dir = settings.BASE_DIR

api_key = "your_api_key"

openai.api_key = api_key


# Function to encode the image
def encode_image(image_path: InMemoryUploadedFile):
    file_content = image_path.read()
    # Encode the file content as base64
    base64_encoded_content = base64.b64encode(file_content)
    # Decode bytes to string (if necessary)
    base64_string = base64_encoded_content.decode("utf-8")
    return base64_string
    # with open(image_path, "rb") as image_file:
    #     return base64.b64encode(image_file.read()).decode("utf-8")


# Path to your image
image_path = "/munch/thinger.png"
real_image_path = str(base_dir) + image_path


def read_image(image_path):
    # Getting the base64 string
    base64_image = encode_image(image_path)
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Output the text in this image. Do NOT output anything else.",
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
        "max_tokens": 300,
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=payload
    )
    print(response.json())
    return response.json()["choices"][0]["message"]["content"]


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
    sugars = 0

    for food in response.json()["foods"]:

        calories += food["nf_calories"]

        protein += food["nf_protein"]

        carbs += food["nf_total_carbohydrate"]
        fats += food["nf_total_fat"]
        if food["nf_sugars"] != None:
            sugars += food["nf_sugars"]

    return {
        "Calories": calories,
        "Protein": protein,
        "Carbs": carbs,
        "Fat": fats,
        "Sugars": sugars,
        "Recipe": food,
    }


def image_to_info(image_path):
    print("infoing")
    return calc_macros(read_image(image_path))


def get_recipe_feedback(recipe):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo-preview",
            messages=[
                {
                    "role": "system",
                    "content": "You are a knowledgeable assistant trained in culinary arts and nutrition. Provide succinct nutrition or cost feedback on the given recipe, with actionable steps to improve the recipe. Do NOT use markdown, so no asterisks or # symbols. NO MARKDOWN!!!!!! DON'T USE IT!!! 3 sentences or less, please.",
                },
                {"role": "user", "content": recipe},
            ],
        )
        # Extracting and returning the assistant's response
        feedback = response["choices"][0]["message"]["content"]
    except:
        feedback = (
            "Sorry, feedback could not be generated at this time. Please try again."
        )
    return feedback
