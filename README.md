# 🥗 Munch.ai

## 📌 Overview
**Munch.ai** is a nutrition-focused web application designed to help users eat healthier by generating calorie-conscious recipes and macro insights based on uploaded ingredient lists or scanned recipes. It leverages AI and nutrition APIs to simplify healthy eating for everyone.

---

## 🚀 Features
- ✅ Upload a recipe photo and get calorie and macro breakdowns using computer vision  
- ✅ Input ingredients manually and receive healthy, AI-curated recipe suggestions  
- ✅ Personalized nutrition advice powered by language models and APIs  
- ✅ Clean, minimalistic interface built for clarity and ease-of-use

---

## 🛠️ Technologies Used

| Area            | Stack/Tools                                           |
|-----------------|-------------------------------------------------------|
| Backend         | Python, Django                                        |
| Frontend        | HTML, CSS, JavaScript                                 |
| AI / ML         | GPT-4 Vision, Nutritionix API                         |
| Image Handling  | OpenCV, PIL                                           |
| Hosting         | PythonAnywhere / Railway / Vercel / Custom Server     |
| Other Tools     | Git, Figma, Postman, Canva                            |

---

## 👨‍💻 My Role

- Designed and implemented the Django backend for ingredient processing  
- Integrated GPT-4 Vision and Nutritionix API for nutrition analysis  
- Collaborated on UI/UX design to ensure an intuitive, aesthetic frontend  
- Ensured app responsiveness and optimized performance across devices  

---

## 📷 Screenshots

<table>
  <tr>
    <td align="center">
      <img src="home.png" width="1000" alt="Dashboard screenshot" /><br/>
    </td>
    <td align="center">
      <img src="ingredients.png" width="1000" alt="Gradebook screenshot" /><br/>
    </td>
  </tr>
</table>

---

## 🧪 How to Run Locally

```bash
# Clone repo
git clone https://github.com/IshanA2007/munch-ai.git
cd munch-ai

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Django server
python manage.py runserver
