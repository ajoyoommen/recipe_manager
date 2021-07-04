from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

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


class IngredientList(ListView):
    template_name = 'ingredients/list.html'
    model = models.Ingredient

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        object_list = self.model.objects.all()
        if q:
            _objs_name = object_list.filter(name__icontains=q)
            _objs_artn = object_list.filter(article_number__icontains=q)
            object_list =  _objs_name | _objs_artn
        print(f'Name: `{q}`, queryset: {object_list}')
        return object_list


def get_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(models.Ingredient, pk=ingredient_id)
    return render(request, 'ingredients/detail.html', {
        'ingredient': ingredient
    })


class CreateIngredient(CreateView):
    model = models.Ingredient
    template_name = 'ingredients/new.html'
    form_class = IngredientForm


class UpdateIngredient(UpdateView):
    model = models.Ingredient
    template_name = 'ingredients/edit.html'
    form_class = IngredientForm
