from django.urls import path

from .views import  LoginView, register

from django.contrib.auth.views import LogoutView

app_name='user'

urlpatterns = [
    # path("register", register, name="register"),
    
   
]