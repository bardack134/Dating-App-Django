from django.conf import settings
from django.urls import path


from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static

from user.views import ProfileCreateView, ProfileUpdateView


app_name='user'

urlpatterns = [
    
    # When a user accesses /profile/new/, the ProfileCreateView is used to display the profile creation form
    path('profile/new/', ProfileCreateView.as_view(), name='profile_create'),
    
    # when this url is accessed, the ProfileUpdateView is used to display the profile edit form for the profile
    # with the specific ID.
    path('profile/<int:pk>/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    
   
]

#TODO: create the templates for the new profile views

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)