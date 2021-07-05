from decimal import Decimal

from crispy_forms.layout import Layout, Submit
from django import forms
from django.forms import inlineformset_factory
from crispy_forms.helper import FormHelper

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'inline_field.html'
        self.helper.layout = Layout(
            'ingredient',
            'quantity',
        )
        self.helper.add_input(Submit('submit', 'Submit'))


IngredientsFormSet = inlineformset_factory(
    Recipe, RecipeIngredient, form=RecipeForm, fields=['ingredient', 'quantity'],
    extra=1)