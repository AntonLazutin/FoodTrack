from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()
  age = forms.IntegerField(label='Возраст')
  height = forms.IntegerField(label='Рост')
  weight = forms.IntegerField(label='Вес')
  gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CustomUser.Gender.choices, label="Пол")
  goal = forms.ChoiceField(widget=forms.RadioSelect, choices=CustomUser.Goal.choices, label="Цель")

  class Meta:
      model = CustomUser
      fields = ['username', 'email', 'first_name', 'weight', 'height', 'age', 'gender', 'goal']


class UserUpdateForm(forms.ModelForm):
    class Meta:
      model = CustomUser
      fields = ['username', 'email', 'first_name', 'weight', 'height', 'age', 'gender', 'goal']