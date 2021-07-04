from decimal import Decimal

from django import forms
from django.forms import inlineformset_factory

from recipes.models import Ingredient, Recipe, RecipeIngredient


CHOICES = (
    (Ingredient.GRAM, '1 gram'),
    (Ingredient.LITER, '1 liter'),
    ('kilogram', '1 kilogram'),
    ('centiliter', '1 centiliter')
)


class IngredientForm(forms.ModelForm):
    unit = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Ingredient
        fields = ['name', 'article_number', 'cost']

    def save(self, commit=True):
        obj = super().save(commit=False)

        cleaned_data = self.cleaned_data
        cost = cleaned_data['cost']
        unit = cleaned_data['unit']

        if unit == 'kilogram':
            factor = Ingredient.FACTOR_GRAM_TO_KG
            unit = 'gram'
        elif unit == 'centiliter':
            factor = Ingredient.FACTOR_LITER_TO_CL
            unit = 'liter'
        else:
            factor = 1
        cost = cost / Decimal(factor)
        obj.cost = round(cost, 4)
        obj.unit = unit
        if commit:
            obj.save()
        return obj


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description')


IngredientsFormSet = inlineformset_factory(
    Recipe, RecipeIngredient, form=RecipeForm, fields=['ingredient', 'quantity'])