# Recipe manager

This is a recipe manager developed with Django

## Installation

    pip install -r requirements.txt
    python manage.py migrate  # Run migrations


## Starting the application

    python manage.py runserver

The application start at port 8000, so it will be accessible at `http://127.0.0.1:8000/recipes/home`

## Usage

This application can be used via the [admin](/admin/recipes) or the [webpage](/recipes/).

* To use via admin, create a super user and login using the user credentials
* To use via the custom webpage, no login is required.

## Features

* Ingredient - List, add and edit 
* Recipe - List, add and view (with cost)

## Todo

* Recipe - Support for multiple ingredients
* Editing a recipe
* Supporting multiple units when adding recipe
* Unit tests
* Dockerfile
