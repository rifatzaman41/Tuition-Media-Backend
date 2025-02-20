from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='student')
    phone= models.CharField(max_length=15)
 #   user=models.OneToOneField(User,on_delete=models.CASCADE)
    #username = models.CharField(max_length=150, unique=True, null=False, blank=False)
    #first_name=models.CharField(max_length=50)
    #last_name=models.CharField(max_length=50)
   # email=models.EmailField(max_length=254)
    #password=models.CharField(max_length=128)
    #confirm_password=models.CharField(max_length=128)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    