from django.contrib import admin
from .models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'job_role', 'address', 'city', 'pincode', 'date')

# Register your models here.
