from django.contrib import admin

from recipes.models import Ingredient, Recipe, RecipeIngredient


class IngredientsInline(admin.TabularInline):
    model = RecipeIngredient
    fk_name = 'recipe'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientsInline, )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display =('name', 'unit', 'cost')


admin.site.register(RecipeIngredient)