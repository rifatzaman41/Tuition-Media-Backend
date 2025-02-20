from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Student
from . import serializers
from rest_framework .views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework import filters
class StudentApiView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer


class AvailableForSPecificStudent(filters.BaseFilterBackend):
      def filter_queryset(self,request,query_set,view):
          user_id=request.query_params.get("user_id")
          if user_id:
              return query_set.filter(user_id=user_id)
          return query_set   

class UserRegistrationApiView(APIView):
    serializer_class=serializers.RegistrationSerializer
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
              user=serializer.save()
              print(user)
              token=default_token_generator.make_token(user)
              print("token", token)         
              uid=urlsafe_base64_encode(force_bytes(user.pk))
              confirm_link=f"http://127.0.0.1:8000/profile1/active/{uid}/{token}"
              email_subject="Confirm Your Email"
              email_body=render_to_string('confirm_email.html',{'confirm_link':confirm_link})
             
              email=EmailMultiAlternatives(email_subject,'',to={user.email})
              email.attach_alternative(email_body,"text/html")
              email.send()
              return Response("check for your mail for confirmation")
        return Response(serializer.errors)
    
def activate(request,uid64,token):
         try:
              uid=urlsafe_base64_decode(uid64).decode()
              user=User._default_manager.get(pk=uid)
         except(User.DoesNotExist):
              user=None

         if user is not None and default_token_generator.check_token(user,token):
              user.is_active=True
              user.save()
              return redirect('login')
         else:
              return redirect('register')    
         

class UserLoginApiView(APIView):
     def post(self,request):
          serializer=serializers.UserLoginSerializer(data=self.request.data)
          if serializer.is_valid(): 
              username=serializer.validated_data['username']
              password=serializer.validated_data['password']
              print(username, password)
              user=authenticate(username=username, password=password)
              print(user)
              if user:
                   token, _=Token.objects.get_or_create(user=user)
                   print(token)                  
                   login(request,user)
                   student = Student.objects.get(user=user)
                   return Response({'token':token.key,'student_id':student.id})
  
              else:
                  
                   return Response({'error':"Invalid Credential"})     
          return Response(serializer.errors)  
     

class UserLogoutView2(APIView):
    def get(self, request):
        print ('User logged',request)
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')


class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"success": "Logged out successfully"})

