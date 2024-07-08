from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView 
from .models import Profile  # Import the Profile model
from .forms import ProfileForm  # Import the ProfileForm form class

# Create your views here.
#TODO: 2.Create views for Registration, Editing and Profile Viewing



# Class-based view for creating a new Profile
class ProfileCreateView(CreateView):
    
    # Specify the model to be used
    model = Profile  
    
    # Specify the form class to be used
    form_class = ProfileForm  
    
    # Specify the template to be used
    template_name = 'profile_form.html' 


# Class-based view for updating an existing Profile
class ProfileUpdateView(UpdateView):
    
    # Specify the model to be used
    model = Profile  
    
    # Specify the form class to be used
    form_class = ProfileForm  
    
    # Specify the template to be used
    template_name = 'profile_form.html'  

