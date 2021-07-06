# Recipe manager

This is a recipe manager developed with Django, bootstrap 5 and django crispy forms

## Installation

1. Setup and activate virtual environment

       cd recipe_manager/
       pip install -r requirements.txt
       python manage.py migrate  # Run migrations


## Starting the application

    python manage.py runserver

The application starts at port 8000, so it will be accessible at `http://127.0.0.1:8000/recipes/`

## Usage

This application can be used via the [admin](/admin/recipes) or the [webpage](/recipes/).

* To use the admin, create a super user and login using the user credentials
* To use via the custom webpage, no login is required.

## Features

* Ingredient - List, add and edit 
* Recipe - List, add and view (with cost)

## Todo

* Editing a recipe ingredients
* Supporting multiple units when adding or editing recipe
* Unit tests
* Dockerfile


## References

* [Inline formsets with crispy forms](https://dev.to/zxenia/django-inline-formsets-with-class-based-views-and-crispy-forms-14o6)