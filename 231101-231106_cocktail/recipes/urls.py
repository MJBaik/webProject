from django.urls import path
from . import views


app_name="cocktails"

urlpatterns = [
    path('', views.index, name="index"),
    path('recipes/', views.recipes, name="recipes")
]
