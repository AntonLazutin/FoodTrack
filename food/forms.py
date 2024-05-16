from django import forms
from .models import Food, MealFood


class FoodForm(forms.ModelForm):
    class Meta:
        model=Food
        fields = "__all__"
    name = forms.CharField(label="Наименование продукта питания", required=True)
    calorie = forms.FloatField(label="Калорийность на 1 грамм продукта", required=True)


class MealFoodForm(forms.ModelForm):
    class Meta:
        model=MealFood
        fields = ['food_id', 'weight']
    food_id = forms.ModelChoiceField(label="Продукт питания", queryset=Food.objects.all(), required=True)
    weight = forms.FloatField(label="Вес в граммах", required=True)