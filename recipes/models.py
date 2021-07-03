from decimal import Decimal

from django.db import models


class Ingredient(models.Model):
    GRAM = 'gram'
    LITER = 'liter'
    
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

class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="quantities")
    quantity = models.FloatField(default=0)
    
    def __str__(self):
        return f'{self.ingredient} in {self.recipe}'

    def get_cost(self):
        return self.ingredient.cost * Decimal(self.quantity)