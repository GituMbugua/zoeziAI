from dataclasses import fields
from email.policy import default
import imp
from sre_parse import CATEGORIES
from tkinter.tix import Tree
from turtle import title
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, CustomerProfile, TrainerProfile, Workout, WorkoutProgram, Contact

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)

GOAL_CHOICES = (
    ('Weight loss', 'Weight loss'), 
    ('Weight gain', 'Weight gain'), 
    ('Strength', 'Strength'), 
    ('Endurance', 'Endurance'), 
    ('Flexibility', 'Flexibility')
)

TARGET_CHOICES = (
    ('Back', 'Back'),
    ('Biceps', 'Biceps'),
    ('Cardio', 'Cardio'), 
    ('Chest', 'Chest'),
    ('Cooldown', 'Cooldown'),
    ('Core', 'Core'),
    ('Legs', 'Legs'),
    ('Shoulders', 'Shoulders'),
    ('Triceps', 'Triceps'),
    ('Warm up', 'Warm up'), 
)

CATEGORY_CHOICES = (
    ('Cardio', 'Cardio'),
    ('Body Weight', 'Body Weight'),
    ('Gym', 'Gym'), 
    ('Yoga', 'Yoga'),
)

BODY_TYPE_CHOICES = (
    ('Ectomorph', 'Ectomorph'),
    ('Mesomorph', 'Mesomorph'), 
    ('Endomorph', 'Endomorph'),
)

FITNESS_LEVEL_CHOICES = (
    ('Beginner', 'Beginner'),
    ('Intermediate', 'Intermediate'), 
    ('Advanced', 'Advanced'),
)

EXPERIENCE_CHOICES = (
    ('Beginner', 'None to 1'),
    ('Intermediate', '1 to 3'), 
    ('Advanced', 'More than 3'),
)

TRAINING_MODE_CHOICES = (
    ('Body Weight', 'Body Weight'),
    ('Weight Training', 'Weight Training'), 
)



class DateInput(forms.DateInput):
    input_type = 'date'

class RegisterForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class UpdateCustomerProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    date_of_birth = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    weight = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), help_text="Enter weight in kilograms")
    height = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), help_text="Enter height in centimeters")
    # body_type = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # fitness_level = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # experience = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # training_mode = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    goal = forms.ChoiceField(choices=GOAL_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomerProfile
        fields = ['avatar', 'date_of_birth', 'gender', 'weight', 'height', 'goal']

class UpdateTrainerProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    date_of_birth = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))


    class Meta:
        model = TrainerProfile
        fields = ['avatar', 'date_of_birth', 'gender', 'location', 'bio']

class AddWorkoutForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    target = forms.ChoiceField(choices=TARGET_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Workout
        fields = ['title', 'description', 'image', 'target']

class AddWorkoutProgramForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    program = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = WorkoutProgram
        fields = '__all__'

class FitnessDetailsForm(forms.ModelForm):
    body_type = forms.ChoiceField(choices=BODY_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), help_text="* See help for details")
    fitness_level = forms.ChoiceField(choices=FITNESS_LEVEL_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    experience = forms.ChoiceField(choices=EXPERIENCE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}), help_text="* Number of years you have been training")
    training_mode = forms.ChoiceField(choices=TRAINING_MODE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomerProfile
        fields = ['body_type', 'fitness_level', 'experience', 'training_mode']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'