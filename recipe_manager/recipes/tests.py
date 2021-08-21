from django.test import TestCase
from django.urls import reverse

from recipes import models


URL_RECIPES = '/recipes/'
URL_RECIPE_ADD = '/recipes/add'
URL_RECIPE = '/recipes/{}'
URL_RECIPE_EDIT = '/recipes/{}/update'

URL_INGREDIENTS = '/recipes/ingredients'
URL_INGREDIENT_ADD = '/recipes/ingredients/add'
URL_INGREDIENT = '/recipes/ingredients/{}'
URL_INGREDIENT_EDIT = '/recipes/ingredients/{}/update'


class URLTests(TestCase):
    def test_recipe_urls(self):
        self.assertEqual(reverse('home'), URL_RECIPES)

        url = reverse('recipe-detail', args=[125])
        self.assertEqual(url, URL_RECIPE.format(125))

        url = reverse('recipe-edit', args=[125])
        self.assertEqual(url, URL_RECIPE_EDIT.format(125))

        self.assertEqual(reverse('recipe-add'), URL_RECIPE_ADD)

    def test_ingredient_urls(self):
        self.assertEqual(reverse('ingredients'), URL_INGREDIENTS)

        url = reverse('ingredient-detail', args=[125])
        self.assertEqual(url, URL_INGREDIENT.format(125))

        url = reverse('ingredient-edit', args=[125])
        self.assertEqual(url, URL_INGREDIENT_EDIT.format(125))

        self.assertEqual(reverse('ingredient-add'), URL_INGREDIENT_ADD)


class RecipeTests(TestCase):

    def test_recipe_urls(self):
        response = self.client.get(URL_RECIPES)
        self.assertEqual(response.status_code, 200)

        url_detail = URL_RECIPE.format(1)
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, 404)

        response = self.client.get(URL_RECIPE_EDIT.format(1))
        self.assertEqual(response.status_code, 404)

    def test_ingredient_urls(self):
        response = self.client.get(URL_INGREDIENTS)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(URL_INGREDIENT.format(1))
        self.assertEqual(response.status_code, 404)

        response = self.client.get(URL_RECIPE_EDIT.format(4))
        self.assertEqual(response.status_code, 404)

    def test_create_ingredient(self):
        obj = models.Ingredient.objects.create(name='Water', cost=0.001, unit=models.Ingredient.LITER)
        obj.save()

        url = URL_INGREDIENT.format(obj.id)
        response = self.client.get(url)
        self.assertEqual(models.Ingredient.objects.all(), url)
        self.assertEqual(response.status_code, 200)
