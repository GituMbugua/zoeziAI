from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(CustomerProfile)
admin.site.register(TrainerProfile)
admin.site.register(Workout)
admin.site.register(WorkoutProgram)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Contact)