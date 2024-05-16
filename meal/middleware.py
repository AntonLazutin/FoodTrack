from django.utils import timezone
from .models import Meal
from datetime import date


class EnsureDefaultMealsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            meals_exist = Meal.objects.filter(user=user, date=date.today()).exists()
            if not meals_exist:
                Meal.objects.create(name='Завтрак', user=user, date=date.today())
                Meal.objects.create(name='Обед', user=user, date=date.today())
                Meal.objects.create(name='Ужин', user=user, date=date.today())
        response = self.get_response(request)
        return response