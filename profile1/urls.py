from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router=DefaultRouter()

router.register('list', views.StudentApiView)
#router.register('logins',views.LoginApiView)
urlpatterns = [
    path("",include(router.urls)),
    path('registers/',views.UserRegistrationApiView.as_view(),name='register'),
    path('logins/',views.UserLoginApiView.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('active/<uid64>/<token>/',views.activate,name='activate'),
]