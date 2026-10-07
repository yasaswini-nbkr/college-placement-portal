from django.contrib import admin
from .models import StudentProfile, Job, Application

admin.site.register(StudentProfile)
admin.site.register(Job)
admin.site.register(Application)