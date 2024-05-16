from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserRegisterForm, UserUpdateForm

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

from meal.models import Meal
from .models import CustomUser


class LoginPageView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('meal_log') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        res = super().form_valid(form)
        self.object.count_calorie_dose()
        self.object.save()
        return res
    

class LogoutPageView(View):

    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect((reverse_lazy('login')))


class ProfileView(View):
    template_name='profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name='profile.html')
    

class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    model = CustomUser
    template_name = 'update.html'
    success_url = reverse_lazy('profile')

    
class LineChartJSONView(BaseLineChartView):

    def get_meals(self):
        meals = Meal.objects.filter(user=self.request.user).order_by('date')
        return meals
    
    def get_calories_by_day(self):
        meals = self.get_meals()
        dates = set(self.get_dates(meals))
        calories = []
        for _date in dates:
            meals_by_date = meals.filter(date=_date)
            calories.append(sum(meal.calorie_sum for meal in meals_by_date))
        return calories

    def get_dates(self, meals):
        dates = [meal.date for meal in meals]
        return sorted(dates)

    def get_labels(self):
        """list(set(list)) для уникальных значений списка"""
        print(self.get_calories_by_day())
        return list(set(self.get_dates(self.get_meals())))

    def get_providers(self):
        return ["Калории за день"]

    def get_data(self):
        return [self.get_calories_by_day()]


line_chart = TemplateView.as_view(template_name='profile.html')
line_chart_json = LineChartJSONView.as_view()