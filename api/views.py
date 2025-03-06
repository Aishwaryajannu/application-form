from django.shortcuts import render
from rest_framework import generics
from .models import JobApplication
from .serializers import JobApplicationSerializer

class JobApplicationListCreate(generics.ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

# Create your views here.
