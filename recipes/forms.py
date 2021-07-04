from decimal import Decimal

from django import forms

from recipes.models import Ingredient


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