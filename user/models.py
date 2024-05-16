from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _



class CustomUser(AbstractUser):

    class Gender(models.TextChoices):
        MALE = 'M', _('Мужской'), 
        FEMALE = 'F',_('Женский')

    class Goal(models.TextChoices):
        LOSS = 'Loss', _('Похудение')
        MAINTAIN = 'Main', _('Поддержание веса')
        GAIN = 'Gain', _('Набор массы')

    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    gender = models.CharField(choices=Gender.choices, default=None, max_length=7, null=True)
    goal = models.CharField(choices=Goal.choices, default=Goal.MAINTAIN, max_length=16)
    calorie_dose = models.IntegerField(default=0)
    is_premium = models.BooleanField(default=False)

    def count_calorie_dose(self):
        if self.id:
            cals = 0
            if self.gender == 'M':
                if self.goal == 'Main':
                    cals = 10 * self.weight + 6.25 * self.height- 5 * self.age + 500
                elif self.goal == 'Loss':
                    cals = 10 * self.weight + 6.25 * self.height- 5 * self.age + 5
                elif self.goal == 'Gain':
                    cals = (self.height * 5) - (self.age * 6.8) + (self.weight * 13.7) + 655
                self.calorie_dose = cals
            elif self.gender == 'F':
                if self.goal == 'Main':
                    cals = 10 * self.weight + 6.25 * self.height- 5 * self.age + 150
                elif self.goal == 'Loss':
                    cals = 10 * self.weight + 6.25 * self.height- 5 * self.age -161
                elif self.goal == 'Gain':
                    cals = 10 * self.weight + 6.25 * self.height- 5 * self.age + 350
            self.calorie_dose = cals


    def save(self, *args, **kwargs):
        self.count_calorie_dose()
        super(CustomUser, self).save(*args, **kwargs)

    
