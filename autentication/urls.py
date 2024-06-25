from django.urls import path

from .views import  LoginView, register


app_name='autentication'

urlpatterns = [
    path("register", register, name="register"),
    
    path('login', LoginView.as_view(), name='login'),
    
    # path('logout', logoutView.as_view(), name='logout'),
]