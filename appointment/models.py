from django.db import models
from profile1.models import Student
from tuition.models import TuitionTeacher,AvailableTime
# Create your models here.
APPOINTMENT_STATUS=[
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Running','Running'),
]
APPOINTMENT_TYPES=[
    ('Offline','Offline'),
    ('Online','Online'),
]
class Appointment(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    teacher=models.ForeignKey(TuitionTeacher,on_delete=models.CASCADE)
    appointment_types=models.CharField(choices=APPOINTMENT_TYPES,max_length=10)
    appointment_status=models.CharField(choices=APPOINTMENT_STATUS,max_length=10,default="Pending")
    symtom=models.TextField()
    time=models.ForeignKey(AvailableTime,on_delete=models.CASCADE)
    cancel=models.BooleanField(default=False)
 

    def __str__(self):
        return f"Teacher : {self.teacher.user.first_name} , Student : {self.student.user.first_name}"
    