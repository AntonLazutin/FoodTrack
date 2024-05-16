from django.urls import path
from . import views

urlpatterns = [
    path('', views.MealViewList.as_view(), name='meal_log'),
    path('<int:pk>', views.MealDetailView.as_view(), name='meal_detail'),
    path('<int:pk>/update', views.MealUpdateView.as_view(), name='meal_update'),
    path('<int:pk>/add', views.MealFoodAdd.as_view(), name='meal_add'),
    path('<int:pk>/delete/<int:meal_food_id>', views.MealFoodUnlink.as_view(), name='meal_food_unlink')
]
