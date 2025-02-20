from rest_framework import serializers
from . import models
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Specialization
        fields='__all__'


class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.AvailableTime
        fields='__all__'


class TuitionTeacherSerializer(serializers.ModelSerializer):
      user=serializers.StringRelatedField(many=False)
      specialization=serializers.StringRelatedField(many=True)
      available_time=serializers.StringRelatedField(many=True)
      class Meta:
        model=models.TuitionTeacher
        fields='__all__'
        
class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.AvailableTime
        fields='__all__'
      
     
  

class ReviewSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.SerializerMethodField()
    teacher_name = serializers.SerializerMethodField()
    class Meta:
        model = models.Review
        fields = ['id', 'reviewer_name', 'teacher_name','teacher','body', 'created', 'rating']  

    def get_reviewer_name(self, obj):
      
        return obj.reviewer.user.first_name
    
        
    
    def get_teacher_name(self,obj):

      return f"{obj.teacher.user.first_name} {obj.teacher.user.last_name}"
       
        