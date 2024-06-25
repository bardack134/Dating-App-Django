from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.views.generic import View

# AuthenticationForm is a class used to create a login form in a web application.
from django.contrib.auth.forms import  AuthenticationForm


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
            
            #NOTE: form.is_valid() check if the user already exits so we don need the following lines, but any way 
            # i didn't deleted it
            # # Check if the username already exists
            # if User.objects.filter(username=username).exists():
                
            #     # Display an information message if the username is taken
            #     messages.info(request, "Username already taken!")
            #     return redirect('autentication:register')
        
        
            # Check if the email is already in use
            if User.objects.filter(email=email).exists():
                
                # Display an information message if the email is already taken
                messages.info(request, "Email already taken!")
                return redirect('autentication:register')
               
                  
            # Create a dictionary of data for the UserCreationForm
            form_data = {
                'username': username,
                'password1': password1,
                'password2': password2
            }    
             
             
            # Create an instance of the UserCreationForm with the data from the dictionary
            form = UserCreationForm(form_data)  
            
              
            #  checks the form data against the form's validation rules.
            # (e.g., the passwords match, an user already exits)
            if form.is_valid():# cleaned_data will always only contain a key for fields defined in the Form,
                
                # Creates an instance of the user without saving it in the database yet.
                user = form.save(commit=False)
                
                # Assigns additional values ​​(email and name) to the user instance.
                user.email = email
                
                # Definitively save the user instance in the database with all the necessary data.
                user.first_name=name
                user.save()
                
                
                # Authenticate the user,  returns a User object if the user exist on the contrary return none
                user = authenticate(username=username, password=password1)
                
                if user is not None:  

                    # Log the user in
                    login(request, user) 

                    
                    # Display an information message
                    messages.success(request, f'Registration successful, Welcome {username}')
                    

                    # Redirect for now to the home page
                    return redirect('homepage:home')

                else:
                    
                    # This shouldn't normally happen because the user was just created,
                    messages.error(request, 'Authentication failed. Please try logging in.')
                    return redirect('autentication:register')
            else:  

                # form.errors is a dictionary-like object where the keys are the field names (e.g., 'username', 'password1',
                # etc.), and the values are lists of error messages associated with those fields.
                for field, errors in form.errors.items():
                    
                    # For each field, there could be multiple error messages.
                    for error in errors:
                        
                        # For each error message,　add an error message to the response
                        messages.error(request, f"{field}: {error}")
                
                # Redirect for now to the home page
                return redirect('autentication:register')
            
            
        #if all fields are not filled return a error to the user
        else:
            
            messages.error(request, 'Please fill all fields')
            
            return redirect('autentication:register')
            
    
    else:
        return render(request, "login.html")


#NOTE: another way to do it
# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.email = form.cleaned_data['email']
#             user.first_name = form.cleaned_data['fullname']
#             user.save()
            
#             # Authenticate and log the user in
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
            
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'Registration successful. You are now logged in.')
#                 return redirect('home')
#         else:
#             for field, errors in form.errors.items():
#                 for error in errors:
#                     messages.error(request, f"{field}: {error}")
#     else:
#         form = RegisterForm()
    
#     return render(request, 'register.html', {'form': form})


class LoginView(View):  

    
    def get(self, request):  
    
        
        form = AuthenticationForm() 

        
        context = {'form': form}  

        
        return render(request, 'login2.html', context)  

    
    def post(self, request):  

        
        form = AuthenticationForm(request, data=request.POST)  

        
        if form.is_valid():  
          
            username = form.cleaned_data.get("username")  

           
            password = form.cleaned_data.get("password") 

           
            user = authenticate(username=username, password=password) 

            if user is not None:  

                login(request, user) 

                #while creating the user profile form I redirect to the home page
                return redirect('homepage:home')

            
            else:  

                messages.error(request, "invalid username or password")
                
                return redirect('autentication:login')
             
        
        else:  
            messages.error(request, "You have entered an invalid username or password")
            
            return redirect('autentication:login')
        
        
        #
        
        