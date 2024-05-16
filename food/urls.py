from django.urls import path
from . import views

urlpatterns = [
    path('/add', views.FoodCreateView.as_view(), name='food_add')
]