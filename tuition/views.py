from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission
from rest_framework import filters,pagination
class SpecializationViewset(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer


class AvailableTimeForSPecificTeacher(filters.BaseFilterBackend):
      def filter_queryset(self,request,query_set,view):
          teacher_id=request.query_params.get("teacher_id")
          print("teacher_id")
          if teacher_id:
              return query_set.filter(teacher=teacher_id)
          return query_set

class AvailableTimeViewset(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends=[AvailableTimeForSPecificTeacher]

class TuitionTeacherPagination(pagination.PageNumberPagination):
    page_size=1
    page_size_query_param=page_size
    max_page_size=100


class TuitionTeacherViewset(viewsets.ModelViewSet):
    queryset = models.TuitionTeacher.objects.all()
    serializer_class = serializers.TuitionTeacherSerializer
    filter_backends=[filters.SearchFilter]
    pagination_class=TuitionTeacherPagination
    search_fields=['user__first_name','user__email','specialization__name']

class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

