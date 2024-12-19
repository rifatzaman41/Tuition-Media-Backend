from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class AppointmentViewset(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer


    # custom query for Patient
    def get_queryset(self):
        queryset=super().get_queryset()
        student_id=self.request.query_params.get('student_id')

        if student_id:
            queryset=queryset.filter(student_id=student_id)
        return queryset
        