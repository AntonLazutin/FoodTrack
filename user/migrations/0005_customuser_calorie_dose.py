# Generated by Django 5.0.4 on 2024-05-14 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_customuser_goal'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='calorie_dose',
            field=models.IntegerField(default=0),
        ),
    ]
