from django.contrib import admin

from .models import Profile

# Register your models here.

# Customizes the admin interface for the profile model
class ProfileAdmin(admin.ModelAdmin):  
    
    # Display fields in the admin view
    list_display = ("user", "gender", "relationship_status", "location")  
    



admin.site.register(Profile, ProfileAdmin) 