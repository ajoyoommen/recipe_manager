from decimal import Decimal

from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    GRAM = 'gram'
    LITER = 'liter'
    FACTOR_GRAM_TO_KG = 1000
    FACTOR_LITER_TO_CL = 1 / 100
    
    UNITS = (
        (GRAM, '1 gram'),
        (LITER, '1 liter')
    )

    name = models.CharField(max_length=255)
    article_number = models.TextField(blank=True, null=True)
    cost = models.DecimalField(
        max_digits=12, decimal_places=4, default=0)
    
    unit = models.CharField(max_length=20, choices=UNITS)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient-detail', kwargs={'ingredient_id': self.pk})
    
    def get_unit_for_display(self):
        if self.unit == self.GRAM:
            return "grams"
        else:
            return "liters"

    def get_units(self):
        units = []
        _base = {
            'unit': self.unit,
            'cost': self.cost
        }
        if self.unit == self.GRAM:
            units.append(_base)
            units.append({
                'unit': 'kilo gram',
                'cost': round(self.cost * Decimal(self.FACTOR_GRAM_TO_KG), 4)
            })
        else:
            units.append({
                'unit': 'centiliter',
                'cost': round(self.cost * Decimal(self.FACTOR_LITER_TO_CL), 4)
            })
            units.append(_base)
        return units



class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    
    def __str__(self):
        return self.name

    def get_cost(self):
        cost_ingds = [i.get_cost() for i in self.quantities.all()]
        return sum(cost_ingds)

    def count_ingredients(self):
        return self.quantities.count()

    def get_initials(self):
        return self.name[0].upper()


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="quantities")
    quantity = models.FloatField(default=0)
    
    def __str__(self):
        return f'{self.ingredient} in {self.recipe}'

    def get_cost(self):
        return self.ingredient.cost * Decimal(self.quantity)