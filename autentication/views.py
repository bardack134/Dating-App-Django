from django.shortcuts import render

# Create your views here.
def register(request):
    
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        print('probando2')
        name = request.POST.get('name')
        print(name)
        return render(request, "login.html")
    
    return render(request, "login.html")