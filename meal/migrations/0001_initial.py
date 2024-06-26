# Generated by Django 5.0.4 on 2024-05-14 21:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.DateField(default=datetime.date(2024, 5, 14))),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('calorie_sum', models.IntegerField(default=0, null=True)),
                ('date', models.DateField(default=datetime.date(2024, 5, 14))),
                ('meal_food_ids', models.ManyToManyField(blank=True, null=True, related_name='meals', to='food.mealfood')),
            ],
        ),
    ]
