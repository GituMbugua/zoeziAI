# Generated by Django 4.0.2 on 2022-03-31 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0013_remove_workout_program_workoutprogram_program_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='image',
            field=models.ImageField(default='/media/workout_images/dumbell_default.png', upload_to='workout_images'),
        ),
    ]