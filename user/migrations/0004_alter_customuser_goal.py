# Generated by Django 5.0.4 on 2024-05-14 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='goal',
            field=models.CharField(choices=[('Похудение', 'Loss'), ('Поддержание веса', 'Maintain'), ('Набор массы', 'Gain')], default='Поддержание веса', max_length=16),
        ),
    ]