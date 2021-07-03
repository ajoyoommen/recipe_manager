from django.shortcuts import render

from recipes import models


def render_all_recipes(request):
    return render(request, 'recipes/home.tpl', {
        'recipes': models.Recipe.objects.all()
    })