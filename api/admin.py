from django.contrib import admin
from django.utils.html import format_html
from .models import JobApplication 
from django.contrib.auth.models import Group, User # Import your JobApplication model

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'job_role', 'address', 'city', 'pincode', 'date')
    list_filter = ('city', 'job_role')  # Optional: Filtering options
    search_fields = ('first_name', 'last_name', 'email', 'job_role', 'city')  # Add search functionality

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Manage Job Applications'}  # Change title
        return super().changelist_view(request, extra_context=extra_context)

# Register the model
admin.site.register(JobApplication, JobApplicationAdmin)

# Hide all other sections in the admin panel
admin.site.site_header = "Job Applications Admin"
admin.site.index_title = ""  # Remove the extra sections
admin.site.site_title = "Job Applications"
