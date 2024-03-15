from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db import models
from .models import Recipe, Ingredient, RecipeIngredient

def recipe_list(request):
    recipe = Recipe.objects.all()
    ctx = {
        'recipes': recipe
    }
    return render(request, 'recipelist.html', ctx)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {
        'recipe': recipe
    }
    return render(request, 'page.html', ctx)

class ledgerListView(ListView):
    model = Recipe
    template_name = 'recipeslist.html'
 
class ledgerDetailView(DetailView):
    model = Recipe
    template_name = 'page.html'

# Create your views here.
