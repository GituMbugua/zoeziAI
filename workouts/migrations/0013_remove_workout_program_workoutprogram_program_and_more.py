# Generated by Django 4.0.2 on 2022-03-31 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0012_workout_program_alter_workout_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='program',
        ),
        migrations.AddField(
            model_name='workoutprogram',
            name='program',
            field=models.TextField(default='Brief workout description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workout',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='workout',
            name='image',
            field=models.ImageField(default='default.png', upload_to='workout_images'),
        ),
        migrations.AlterField(
            model_name='workoutprogram',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
