from django import forms
from .models import Meal
from food.models import MealFood


class MealUpdateForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['meal_food_ids',]

    meal_food_ids = forms.ModelMultipleChoiceField(
        queryset=MealFood.objects.all(),
        label="Ранее добавленные продукты",
        widget=forms.SelectMultiple(attrs={'class': 'select2', 'data-live-search': 'true'})
    )