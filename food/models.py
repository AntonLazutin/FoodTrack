from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=30)
    calorie = models.FloatField(default=0)


    def __str__(self):
        return self.name
    

class MealFood(models.Model):
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    weight = models.FloatField(default=0)
    calorie = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        calorie = self.food_id.calorie * self.weight
        self.calorie = calorie
        super(MealFood, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.food_id.name} {self.weight} г.'
