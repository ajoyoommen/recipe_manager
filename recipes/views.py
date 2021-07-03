from django.shortcuts import render

from recipes import models


def home(request):
    return render(request, 'home.html', {
        'recipes': models.Recipe.objects.all()
    })