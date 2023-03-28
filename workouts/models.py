from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    is_customer = models.BooleanField(default=True)
    is_trainer = models.BooleanField(default=False)

    @classmethod
    def get_customers(cls):
        customers = cls.objects.filter(cls.is_customer == True)
        return customers

    @classmethod
    def get_trainers(cls):
        trainers = cls.objects.filter(cls.is_trainers == True)
        return trainers

class Workout(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(default='workout_images/dumbell_default.png', upload_to='workout_images', null=True, blank=True)
    target = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @classmethod
    def get_workouts(cls):
        workouts = cls.objects.all()
        workouts = cls.objects.order_by('title')
        return workouts

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @classmethod
    def get_tags(cls):
        tags = cls.objects.all()
        return tags

class WorkoutProgram(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    program = models.TextField()
    category = models.CharField(blank=True, max_length=100)
    tags = models.ManyToManyField(Tag, blank=True)
    workouts = models.ManyToManyField(Workout, blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_workout_programs(cls):
        program = cls.objects.all()
        program = cls.objects.order_by('title')
        return program
    
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, related_name='customer_profile', on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.png', upload_to='profile_images')
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20)
    weight = models.PositiveIntegerField(default=0)
    height = models.PositiveIntegerField(default=0)
    body_type = models.CharField(max_length=100)
    fitness_level = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    training_mode = models.CharField(max_length=100)
    goal = models.CharField(max_length=100)
    program = models.ManyToManyField(WorkoutProgram, blank=True)

    def __str__(self):
        return self.user.username

class TrainerProfile(models.Model):
    user = models.OneToOneField(User, related_name='trainer_profile', on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.png', upload_to='profile_images')
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30)
    bio = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
