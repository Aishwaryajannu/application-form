from django.urls import path
from .views import JobApplicationListCreate

urlpatterns = [
    path('applications/', JobApplicationListCreate.as_view(), name='applications'),
]
