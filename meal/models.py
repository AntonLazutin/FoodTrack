from django.db import models
from food.models import Food, MealFood
from user.models import CustomUser
from datetime import date
from django.db.models import Sum


class Meal(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    meal_food_ids = models.ManyToManyField(MealFood, null=True, blank=True, related_name='meals')
    calorie_sum = models.FloatField(null=True, default=0)
    date = models.DateField(default=date.today())

    def __str__(self):
        return self.name
    
    def count_cals(self):
        calorie_sum = sum(meal_food.calorie for meal_food in self.meal_food_ids.all())
        self.calorie_sum = calorie_sum
        self.save()
        
class MealCategory(models.Model):
    name = models.CharField(max_length=20)  
    date = models.DateField(default=date.today())
    