from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from .views import ledgerDetailView, ledgerListView #might need to change import of recipe1 etc

urlpatterns = [
	path('recipes/list/', ledgerListView.as_view(),name='recipeslist'),
	path('recipe/<int:pk>/detail', ledgerDetailView.as_view(), name='recipe'),
]

app_name = 'ledger'