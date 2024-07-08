import pprint
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.views.generic import View

# AuthenticationForm is a class used to create a login form in a web application.
from django.contrib.auth.forms import  AuthenticationForm

# This decorator is used to restrict access to a view to only authenticated users.
from django.contrib.auth.decorators import login_required

# This utility is used to apply function-based decorators, like login_required, 
# to methods within class-based views (CBVs).
from django.utils.decorators import method_decorator


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


#NOTE: another way to do register view
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

    # Handle GET requests
    def get(self, request):
        
        # Create an instance of the authentication form
        form = AuthenticationForm()

        # Create the context dictionary with the form
        context = {'form': form}

        # Render the login page with the context
        return render(request, 'login.html', context)

    # Handle POST requests
    def post(self, request):
        
        # Create an instance of the authentication form with posted data
        form = AuthenticationForm(request, data=request.POST)

        
        # Verifies that all required fields are present and meet the specific validation requirements for each field
        # (for example, that an email address is in the correct format).
        if form.is_valid():
            
            # Get the cleaned username from the form data
            username = form.cleaned_data.get("username")

            # Get the cleaned password from the form data
            password = form.cleaned_data.get("password")

            # Authenticate the user with the provided credentials
            user = authenticate(username=username, password=password)

            # If the user is authenticated successfully
            if user is not None:
                
                # Log the user in
                login(request, user)

                # Redirect to the homepage after successful login
                return redirect('homepage:home')
            
            else:
                
                # If authentication fails, show an error message
                messages.error(request, "Invalid username or password")

                # Redirect back to the login page
                return redirect('autentication:login')
            
        else:
            # If there are errors, is_valid() will add these errors to an attribute called errors on the form.
            # For debugging purposes, print form errors
            pprint.pp(form.errors)

            # Create the context dictionary with the form
            context = {'form': form}

            # Re-render the login page with the form and errors
            return render(request, 'login.html', context)




#@login_required(login_url='/autenticacion/login/')
@method_decorator(login_required, name='dispatch')
class RegisterPatientSP(View):

    # Método GET para mostrar o crear el formulario de registro.
    def get(self, request):

        pass
        # # Creamos una instancia del formulario personalizado.
        # form = PatientInformationFormSP()

        # # Preparamos los datos del formulario para pasar al contexto.
        # context = {
        #     'formSP': form 
        # }

        # # Mostramos la página de registro con el formulario.
        # return render(request, 'registro/registro.html', context) 


    def post(self, request):
        
        pass
        # # Creamos una instancia del formulario con los datos del POST.
        # form = PatientInformationFormSP(request.POST)  

        # # Verificamos si los datos ingresados en el formulario son válidos.
        # if form.is_valid():

          
        #     """
        #     #para que el usuario logee automaticamente
        #     usuario=form.save()
        #     login(request, usuario)
        #     """
        #     # Guarda el formulario en la base de datos
        #     patient = form.save()  # Esto guarda los datos en la base de datos y devuelve el objeto creado


        #     # Mostramos un mensaje de éxito.
        #     messages.success(request, 'Paciente registrado exitosamente.')  

        #     # Redirige a la misma vista de registro
        #     return redirect('RegistroPaciente')  

        # context = {
        #     # Preparamos los datos del formulario (incluso si no es válido) para pasar al contexto.
        #     'form': form  
        # }

        # #Mostramos la página de registro con el formulario y posibles errores.
        # return render(request, 'registro/registro.html', context)  