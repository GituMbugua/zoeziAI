# Generated by Django 4.0.2 on 2022-03-26 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_workout_workoutprogram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=True),
        ),
    ]