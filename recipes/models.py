from django.db import models


class Ingredient(models.Model):
    GRAM = 'gram'
    LITER = 'liter'
    
    UNITS = (
        (GRAM, 'grams'),
        (LITER, 'liters')
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
    

class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    
    def __str__(self):
        return f'{self.ingredient} in {self.recipe}'