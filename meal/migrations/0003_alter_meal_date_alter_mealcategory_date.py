# Generated by Django 5.0.4 on 2024-05-15 00:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateField(default=datetime.date(2024, 5, 15)),
        ),
        migrations.AlterField(
            model_name='mealcategory',
            name='date',
            field=models.DateField(default=datetime.date(2024, 5, 15)),
        ),
    ]
