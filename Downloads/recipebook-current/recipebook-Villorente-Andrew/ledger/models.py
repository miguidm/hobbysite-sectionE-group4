from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    short_bio = models.TextField()

class Ingredient(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:ingredient', args=[self.pk])

class Recipe(models.Model):
    author = models.CharField(max_length=60, default="author")
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def author_name(self):
        return self.author

    def get_absolute_url(self):
       return reverse('ledger:recipe', args=[self.pk])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=60)
    ingredient = models.ForeignKey(
        'Ingredient', 
        on_delete=models.CASCADE, 
        related_name="recipe"
        )
    recipe = models.ForeignKey(
        'Recipe', 
        on_delete=models.CASCADE, 
        related_name="ingredients"
        )
