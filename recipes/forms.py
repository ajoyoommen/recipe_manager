from decimal import Decimal

from django import forms
from django.forms import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit

from recipes.custom_layout import Formset
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


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ('ingredient', 'quantity')


IngredientsFormSet = inlineformset_factory(
    Recipe, RecipeIngredient, form=RecipeIngredientForm, fields=['ingredient', 'quantity'],
    extra=1, can_delete=True)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('description'),
                Fieldset('Add ingredients',
                    Formset('formset')),
                HTML("<br>"),
                Submit('submit', 'Save recipe', css_class="btn-primary bg-rm-main my-3"),
                )
            )