from django.urls import path

from recipes import views


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<int:pk>', views.RecipeDetail.as_view(), name='recipe-detail'),
    path('<int:pk>/update', views.EditRecipe.as_view(), name='recipe-edit'),
    path('add', views.AddRecipe.as_view(), name='recipe-add'),

    path('ingredients', views.IngredientList.as_view(), name='ingredients'),
    path('ingredients/<int:pk>', views.IngredientDetail.as_view(), name='ingredient-detail'),
    path('ingredients/<int:pk>/update', views.EditIngredient.as_view(), name='ingredient-edit'),
    path('ingredients/add', views.AddIngredient.as_view(), name='ingredient-add')
]
