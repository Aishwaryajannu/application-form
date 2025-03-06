from django.urls import path
from .views import JobApplicationListCreate

urlpatterns = [
    path('applications/', JobApplicationListCreate.as_view(), name='applications'),
    path('submit-form/', JobApplicationListCreate.as_view(), name='submit-form'),
]
