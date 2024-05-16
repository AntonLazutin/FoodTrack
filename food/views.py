from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Food
from .forms import FoodForm


class FoodCreateView(LoginRequiredMixin, CreateView):
    model = Food
    login_url = '/'
    template_name = 'food_add.html'
    model = Food
    form_class = FoodForm
    success_url = reverse_lazy('meal_log')