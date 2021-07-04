from django.urls import path

from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('recipe/<int:recipe_id>', views.get_recipe, name='recipe-detail'),
    path('ingredients', views.get_ingredients, name='ingredients'),
    path('ingredient/<int:ingredient_id>', views.get_ingredient, name='ingredient-detail'),
    path('ingredient/<int:pk>/update', views.UpdateIngredient.as_view(), name='ingredient-edit'),
    path('ingredient/add', views.CreateIngredient.as_view(), name='ingredient-add')
]