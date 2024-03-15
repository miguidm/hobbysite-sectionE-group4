from django.contrib import admin
from .models import Recipe,RecipeIngredient

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile



class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False


class RecipeIngredientInline(admin.TabularInline):
	model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
	model = Recipe
	inlines = [RecipeIngredientInline,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Recipe, RecipeAdmin)
