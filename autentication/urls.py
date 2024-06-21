from django.urls import path

from . import views

app_name='autentication'

urlpatterns = [
    path("register", views.register, name="register"),
]