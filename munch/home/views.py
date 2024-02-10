from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

class IngredientView(TemplateView):
    template_name = "ingredient.html"

class RecipeView(TemplateView):
    template_name = "recipe.html"
    