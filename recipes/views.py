from django.shortcuts import get_object_or_404, render

from recipes import models


def home(request):
    return render(request, 'home.html', {
        'recipes': models.Recipe.objects.all()
    })


def get_recipe(request, recipe_id):
    recipe = get_object_or_404(models.Recipe, pk=recipe_id)
    return render(request, 'recipe.html', {
        'recipe': recipe
    })