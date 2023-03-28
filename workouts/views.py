from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required

from .forms import RegisterForm, UpdateUserForm, UpdateCustomerProfileForm, UpdateTrainerProfileForm, AddWorkoutForm, AddWorkoutProgramForm, FitnessDetailsForm, ContactForm
from .models import Workout, WorkoutProgram, User

def index(request):
    return render(request, 'workouts/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'workouts/register.html', {'form': form})

@login_required
def customer_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        customer_profile_form = UpdateCustomerProfileForm(request.POST, request.FILES, instance=request.user.customer_profile)

        if user_form.is_valid() and customer_profile_form.is_valid():
            user_form.save()
            customer_profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='customer-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        customer_profile_form = UpdateCustomerProfileForm(instance=request.user.customer_profile)

    return render(request, 'workouts/customer_profile.html', {'user_form': user_form, 'customer_profile_form': customer_profile_form})

def email_request(request):
    user = request.user
    workout_program = user.customer_profile.program.last()

    subject = 'Current Workout Program'
    message = f'Hi {user.first_name}, thank you for working with zoeziAI. Here is your current workout. \n{workout_program.program}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email, ]
    send_mail( subject, message, email_from, recipient_list )
    messages.success(request, 'Email Sent!')
    return redirect(to='customer-profile')

@login_required
@staff_member_required
def trainer_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        trainer_profile_form = UpdateTrainerProfileForm(request.POST, request.FILES, instance=request.user.trainer_profile)

        if user_form.is_valid() and trainer_profile_form.is_valid():
            user_form.save()
            trainer_profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='trainer-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        trainer_profile_form = UpdateTrainerProfileForm(instance=request.user.trainer_profile)

    return render(request, 'workouts/trainer_profile.html', {'user_form': user_form, 'trainer_profile_form': trainer_profile_form})

def about_us(request):
    return render(request, 'workouts/about.html')

def categories(request):
    return render(request, 'workouts/categories.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent.')
            return redirect(to='contact')
    else:
        form = ContactForm()

    return render(request, 'workouts/contact.html', {'form': form})

@login_required
def workouts(request):
    workouts = Workout.get_workouts()

    if request.method == 'POST':
        form = AddWorkoutForm(request.POST, request.FILES)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            messages.success(request, 'Exercise added successfully')
            return redirect(to='workouts')
    else:
        form = AddWorkoutForm()

    return render(request, 'workouts/workouts.html', {'form': form, 'workouts': workouts})

@login_required
def workout_programs(request):
    all_programs = WorkoutProgram.get_workout_programs()

    user_profile = request.user.customer_profile
    body_type = user_profile.body_type.lower()
    experience = user_profile.experience.lower()
    mode = user_profile.training_mode.lower()

    search_list = [experience, mode]
    selected_programs = WorkoutProgram.objects.filter(tags__name__in=search_list).distinct()

    if request.method == 'POST':
        form = AddWorkoutProgramForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(to='workout-programs')
    else:
        form = AddWorkoutProgramForm()

    return render(request, 'workouts/workout_programs.html', {'programs': all_programs, 'form': form, 'selected_programs': selected_programs})

@login_required
def select_workout_program(request, program_id):
    request.user.customer_profile.program.add(program_id)

    return redirect(to='customer-profile')

@login_required
def workout_program_details(request, program_id):
    program = WorkoutProgram.objects.get(id=program_id)
    return render(request, 'workouts/workout_program_details.html', {'program': program})

@login_required
def fitness_details(request):
    if request.method == 'POST':
        form = FitnessDetailsForm(request.POST or None, instance=request.user.customer_profile)
        if form.is_valid():
            form.save()
            return redirect(to='workout-programs')
    else:
        form = FitnessDetailsForm(instance=request.user.customer_profile)

    return render(request, 'workouts/fitness_details.html', {'form': form})

@login_required
def complete_workout(request, program_id):
    request.user.customer_profile.program.remove(program_id)

    return redirect(to='customer-profile')

@login_required
@staff_member_required
def reports(request):
    trainers = User.objects.filter(is_trainer=True)
    customers = User.objects.filter(is_customer=True)
    trainers_count = trainers.count()
    customer_count = customers.count()
    workouts_count = Workout.objects.all().count()
    programs_count = WorkoutProgram.objects.all().count()


    return render(request, 'workouts/reports.html', {
        'trainers_count': trainers_count,
        'customers_count': customer_count,
        'workouts_count': workouts_count,
        'programs_count': programs_count,
        'trainers': trainers,
        'customers': customers,
        })
