from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
# Import the Profile model from the current app's models
from .models import Profile 
from django import forms


#TODO: Define forms using Django Forms to handle the creation and editing of user profiles.


# Define a form class for the Profile model
class ProfileForm(forms.ModelForm):
    
    # Inner Meta class to specify the model and fields
    class Meta:
        
        # specify the name of model to use
        model = Profile  
        
        # Define the fields to include in the form
        fields = ['biography', 'gender', 'relationship_status', 'location', 'citylat', 'citylong', 'birth_date', 'image'] 


#TODO: add custom validations to ensure that the data entered by the user is correct, such as date of birth, not in the future or an imaginary city