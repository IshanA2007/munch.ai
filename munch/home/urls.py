from django.urls import path

from . import views
from .views import *

app_name = "home"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("ingredients/", IngredientView.as_view(), name="ingredients"),
    path("recipes/", RecipeView.as_view(), name="recipes"),
]