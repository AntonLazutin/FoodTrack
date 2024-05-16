from typing import Any
from datetime import date

from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, CreateView, View
from django.views.generic.edit import ProcessFormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import Meal
from .forms import MealUpdateForm

from food.forms import MealFoodForm
from food.models import MealFood


class MealViewList(LoginRequiredMixin, ListView):
    login_url = '/'
    template_name = 'meal_log.html'
    model = Meal

    def calc_percent(self, calories_total):
        if self.request.user.calorie_dose:
            return (calories_total * 100) / self.request.user.calorie_dose
        else:
            return 0
    
    def get_date(self):
        _date = date.today()
        if self.request.GET.get("date"):
            _date = self.request.GET.get("date")
        return _date
 
    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        return qs.filter(date=self.get_date(), user=self.request.user)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        _date = self.get_date()
        ctx['date'] = _date
        meals = Meal.objects.filter(user=self.request.user, date=_date)
        calories_total = sum(meal.calorie_sum for meal in meals)
        ctx['calories_total'] = calories_total
        ctx['percentage'] = self.calc_percent(calories_total)
        return ctx


class MealDetailView(LoginRequiredMixin, DetailView):
    login_url = '/'
    template_name = 'meal_detail.html'
    model = Meal


class MealUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    template_name = 'meal_update.html'
    model = Meal
    form_class = MealUpdateForm
    success_url = reverse_lazy('meal_log')

    def get_context_data(self,**kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['meal_id'] = self.kwargs['pk']
        return ctx
    
    def post(self, request, *args, **kwargs):
        res = super(MealUpdateView, self).post(request, *args, **kwargs)
        meal = Meal.objects.get(pk=self.kwargs['pk'])
        meal.count_cals()
        return res
    

class MealFoodAdd(LoginRequiredMixin, CreateView):
    login_url = '/'
    template_name = 'meal_add.html'
    model = MealFood
    form_class = MealFoodForm
    success_url = reverse_lazy('meal_log')

    
    def form_valid(self, form):
        res = super().form_valid(form)
        linked_meal = Meal.objects.get(pk=self.kwargs['pk'])
        linked_meal.meal_food_ids.add(self.object.id)
        linked_meal.count_cals()
        return res


class MealFoodUnlink(View):

    success_url = reverse_lazy('meal_log')

    def get(self, *args, **kwargs):
        ...

    def post(self, *args, **kwargs):
        try:
            meal = Meal.objects.get(pk=self.kwargs["pk"])
            meal_food = MealFood.objects.get(pk=self.kwargs["meal_food_id"])
            meal.meal_food_ids.remove(meal_food)
            meal.count_cals()
        except Exception as e:
            print(e)
        
        return HttpResponseRedirect(reverse_lazy('meal_log'))
