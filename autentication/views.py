from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

# Create your views here.
def register(request):
    
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        
        # Get data from the form
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Validate that all fields are filled
        if name and username and email and password1 and password2 != None:
            
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                
                # Display an information message if the username is taken
                messages.info(request, "Username already taken!")
                return redirect('/register/')
        
        
            # Check if the email is already in use
            if User.objects.filter(email=email).exists():
                
                # Display an information message if the email is already taken
                messages.info(request, "Email already taken!")
                return redirect('/register/')
               
                
            # Create an instance of the UserCreationForm with the data from the dictionary
            form = UserCreationForm(form_data)  
            
              
            # Create a dictionary of data for the UserCreationForm
            form_data = {
                'username': username,
                'password1': password1,
                'password2': password2
            }    
               
            #  checks the data against the form's validation rules.
            # (e.g., the passwords match, the username is unique)
            if form.is_valid():
                
                # Creates an instance of the user without saving it in the database yet.
                user = form.save(commit=False)
                
                # Assigns additional values ​​(email and name) to the user instance.
                user.email = email
                
                # Definitively save the user instance in the database with all the necessary data.
                user.first_name=name
                user.save()
                
                
                # Authenticate the user,  returns a User object if the user exist on the contrary return none
                user = authenticate(username=username, password=password1)
                
                
                
        #if all fields are not filled return a error to the user
        else:
            messages.error(request, 'Please fill all fields')
            return redirect('register')
            
        return render(request, "login.html")
    
    return render(request, "login.html")



#TODO:use UserCreationForm to be able to check if the data is correct or no