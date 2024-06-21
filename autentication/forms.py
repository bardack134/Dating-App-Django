from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# This class inherits from UserCreationForm,and adding new fields
class RegisterForm(UserCreationForm):
    # Capture the user's email address and user full name
    email = forms.EmailField(label = "Email")
    fullname = forms.CharField(label = "Name")

    # Defines additional settings for the form
    class Meta:
        # Specifies that the form is based on the User model
        model = User
        
        # A list of fields to include in the form
        fields = ("username", "fullname", "email", )