from django.urls import path

from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('recipe/<int:recipe_id>', views.get_recipe, name='recipe-detail'),
    path('recipe/add', views.AddRecipe.as_view(), name='recipe-add'),
    path('recipe/<int:recipe_id>/update', views.EditRecipe.as_view(), name='recipe-edit'),
    path('ingredients', views.IngredientList.as_view(), name='ingredients'),
    path('ingredient/<int:ingredient_id>', views.get_ingredient, name='ingredient-detail'),
    path('ingredient/<int:pk>/update', views.EditIngredient.as_view(), name='ingredient-edit'),
    path('ingredient/add', views.AddIngredient.as_view(), name='ingredient-add')
]