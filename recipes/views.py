from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from recipes import models
from recipes.forms import FORMSET_NAME, IngredientForm, IngredientsFormSet, RecipeForm


def home(request):
    return render(request, 'home.html', {
        'recipes': models.Recipe.objects.order_by('name')
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
        object_list = self.model.objects.order_by('name')
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


class AddIngredient(CreateView):
    model = models.Ingredient
    template_name = 'ingredients/add.html'
    form_class = IngredientForm


class EditIngredient(UpdateView):
    model = models.Ingredient
    template_name = 'ingredients/edit.html'
    form_class = IngredientForm


class AddRecipe(CreateView):
    model = models.Recipe
    template_name = 'recipes/add.html'
    form_class = RecipeForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data[FORMSET_NAME] = IngredientsFormSet(self.request.POST)
        else:
            data[FORMSET_NAME] = IngredientsFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context[FORMSET_NAME]
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)
    
    
class EditRecipe(UpdateView):
    model = models.Recipe
    template_name = 'recipes/edit.html'
    form_class = RecipeForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data[FORMSET_NAME] = IngredientsFormSet(self.request.POST, instance=self.object)
        else:
            data[FORMSET_NAME] = IngredientsFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context[FORMSET_NAME]
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)