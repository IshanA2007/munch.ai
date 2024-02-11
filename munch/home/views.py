from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from .forms import TextInputForm, ImageUploadForm
from . import api_calls


class HomeView(TemplateView):
    template_name = "home.html"


class IngredientView(TemplateView):
    template_name = "ingredient.html"


class SubmitView(View):
    def get(self, request):
        form = TextInputForm()
        return render(request, "text_input.html", {"form": form, "result": None})

    def post(self, request):
        form = TextInputForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data["text_input"]
            result = api_calls.calc_macros(input_text)
            rec = api_calls.get_recipe_feedback(str(result))
        else:
            rec = None
            result = None
        return render(
            request,
            "upload.html",
            {
                "form": form,
                "result": result,
                "cals": result["Calories"],
                "fats": result["Fat"],
                "protein": result["Protein"],
                "carbs": result["Carbs"],
                "sugars": result["Sugars"],
                "rec": rec
            },
        )


class RecipeView(View):
    def get(self, request):
        form = ImageUploadForm()
        return render(request, "upload.html", {"form": form, "result": None})

    def post(self, request):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.cleaned_data["image"]
            
            result = api_calls.image_to_info(uploaded_image)
            rec = api_calls.get_recipe_feedback(str(result))
        else:
            rec = None
            result = None
        return render(
            request,
            "upload.html",
            {
                "form": form,
                "result": result,
                "cals": result["Calories"],
                "fats": result["Fat"],
                "protein": result["Protein"],
                "carbs": result["Carbs"],
                "sugars": result["Sugars"],
                "rec": rec
            },
        )
