# Generated by Django 4.0.2 on 2022-03-31 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0010_workoutprogram_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='workoutprogram',
            name='tags',
            field=models.ManyToManyField(blank=True, to='workouts.Tag'),
        ),
    ]