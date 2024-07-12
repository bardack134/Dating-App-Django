from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView 
from .models import Profile  # Import the Profile model
from .forms import ProfileForm  # Import the ProfileForm form class
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

# Create your views here.
#TODO: 2.Create views for Registration, Editing and Profile Viewing



@method_decorator(login_required, name='dispatch')#Only authenticated users can access these views
class ProfileCreateView(CreateView):# Class-based view for creating a new Profile
    
    # Specify the model to be used
    model = Profile  
    
    # Specify the form class to be used
    form_class = ProfileForm  
    
    # Specify the template to be used
    template_name = 'profileform.html' 

    def get_initial(self):
        # get_initial return a dictionary where the keys are the names of the fields on the form and 
        # the values are the initial values to use when showing the form to the user.
        
        initial = super().get_initial() #Return the initial data to use for the form on this view.
        
        # Sets the initial values ​​of the 'biography, gender.. etc' fields with the value of the current user's profile.
        initial['biography'] = self.request.user.profile.biography
        
        initial['gender'] = self.request.user.profile.gender
        
        initial['relationship_status'] = self.request.user.profile.relationship_status
        
        initial['location'] = self.request.user.profile.country
        
        initial['city'] = self.request.user.profile.city
        
        initial['birth_date'] = self.request.user.profile.birth_date
        
        # more information here 
        # https://stackoverflow.com/questions/22083218/django-how-to-pre-populate-formview-with-dynamic-non-model-data
        return initial

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.user = self.request.user 
        
        # Call the form_valid method of the super class to handle form saving and redirection.
        return super().form_valid(form)

#Only authenticated users can access these views
@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):# Class-based view for updating an existing Profile
    
    # Specify the model to be used
    model = Profile  
    
    # Specify the form class to be used
    form_class = ProfileForm  
    
    # Specify the template to be used
    template_name = 'templates/profileform.html'  


#TODO:1crear "create template "
#TODO:2crear detail view
#TODO:3 crear  detail view template


