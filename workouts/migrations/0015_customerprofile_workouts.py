# Generated by Django 4.0.2 on 2022-03-31 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0014_alter_workout_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='workouts',
            field=models.ManyToManyField(blank=True, to='workouts.WorkoutProgram'),
        ),
    ]
