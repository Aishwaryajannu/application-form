from django.shortcuts import render
from rest_framework import generics
from .models import JobApplication
from .serializers import JobApplicationSerializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
import logging
logger = logging.getLogger(__name__)

class JobApplicationListCreate(generics.ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        logger.info("Received Data: %s", request.data)  # Log request data
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Validation Errors: %s", serializer.errors)  # Log errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
