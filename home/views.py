from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render


# ...
def home(request):
    
    return render(request, "index.html")