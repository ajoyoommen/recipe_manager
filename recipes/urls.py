from django.urls import path

from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('recipe/<int:recipe_id>', views.get_recipe, name='recipe-detail')
]