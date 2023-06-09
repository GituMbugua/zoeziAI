# Generated by Django 4.0.2 on 2022-03-29 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_alter_user_is_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='image',
            field=models.ImageField(blank=True, upload_to='workout_images'),
        ),
        migrations.AddField(
            model_name='workout',
            name='target',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='profile_images'),
        ),
        migrations.RemoveField(
            model_name='workoutprogram',
            name='workouts',
        ),
        migrations.AddField(
            model_name='workoutprogram',
            name='workouts',
            field=models.ManyToManyField(blank=True, to='workouts.Workout'),
        ),
    ]
