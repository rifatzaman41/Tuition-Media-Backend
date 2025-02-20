from django.shortcuts import render
from rest_framework import viewsets
from django.template.loader import render_to_string
from . import models
from . import serializers


# Create your views here.
class AppointmentViewset(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer


    def create(self, request, *args, **kwargs):
        print("Incoming request data:", request.data) 
        return super().create(request, *args, **kwargs)
