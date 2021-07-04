from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView

from recipes import models
from recipes.forms import IngredientForm


def home(request):
    return render(request, 'home.html', {
        'recipes': models.Recipe.objects.all()
    })


def get_recipe(request, recipe_id):
    recipe = get_object_or_404(models.Recipe, pk=recipe_id)
    return render(request, 'recipes/detail.html', {
        'recipe': recipe
    })


def get_ingredients(request):
    ingredients = models.Ingredient.objects.all()
    return render(request, 'ingredients/list.html', {
        'ingredients': ingredients
    })

def get_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(models.Ingredient, pk=ingredient_id)
    return render(request, 'ingredients/detail.html', {
        'ingredient': ingredient
    })


class CreateIngredient(CreateView):
    model = models.Ingredient
    template_name = 'ingredients/new.html'
    form_class = IngredientForm
