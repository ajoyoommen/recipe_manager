from django.contrib import admin

from recipes.models import Ingredient, Recipe, RecipeIngredient


class IngredientsInline(admin.TabularInline):
    model = RecipeIngredient
    fk_name = 'recipe'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientsInline, )


admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)