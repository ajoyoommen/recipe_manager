from django.db import transaction
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from recipes import models
from recipes.forms import FORMSET_NAME, IngredientForm, IngredientsFormSet, RecipeForm


class RecipeList(ListView):
    model = models.Recipe
    template_name = 'home.html'
    context_object_name = 'recipes'
    ordering = ['name']


class RecipeDetail(DetailView):
    queryset = models.Recipe.objects.prefetch_related('ingredients__ingredient')
    template_name = 'recipes/detail.html'


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
        return object_list


class IngredientDetail(DetailView):
    model = models.Ingredient
    template_name = 'ingredients/detail.html'


class AddIngredient(CreateView):
    model = models.Ingredient
    template_name = 'ingredients/add.html'
    form_class = IngredientForm


class EditIngredient(UpdateView):
    model = models.Ingredient
    template_name = 'ingredients/edit.html'
    form_class = IngredientForm


class AddRecipe(CreateView):
    queryset = models.Recipe.objects.prefetch_related('ingredients__ingredient')
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
    queryset = models.Recipe.objects.prefetch_related('ingredients__ingredient')
    template_name = 'recipes/edit.html'
    form_class = RecipeForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data[FORMSET_NAME] = IngredientsFormSet(self.request.POST, instance=self.object)
        else:
            data[FORMSET_NAME] = IngredientsFormSet(instance=self.object)
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
