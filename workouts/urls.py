from urllib.parse import urlparse
from django.urls import URLPattern, path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='workouts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', views.about_us, name='about'),
    path('categories/', views.categories, name='categories'),
    path('contact/', views.contact, name='contact'),
    path('profile/customer/', views.customer_profile, name='customer-profile'),
    path('profile/customer/email-request', views.email_request, name='email-request'),
    path('profile/staff/', views.trainer_profile, name='trainer-profile'),
    path('profile/staff/reports', views.reports, name='reports'),
    path('workouts/', views.workouts, name='workouts'),
    path('workout-programs/', views.workout_programs, name='workout-programs'),
    path('workout-programs/fitness-details', views.fitness_details, name='fitness-details'),
    path('workout-programs/select-program/<int:program_id>', views.select_workout_program, name='select-workout-program'),
    path('workout-program-details/<int:program_id>', views.workout_program_details, name='workout-program-details'),
    path('workout-programs/complete-workout/<int:program_id>', views.complete_workout, name='complete-workout'),
    
]