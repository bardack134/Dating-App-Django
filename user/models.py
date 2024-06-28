from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.expressions import RawSQL
import os
import uuid
# Create your models here.

class LocationManager(models.Manager):
    """Provides a way to get nearby locations sorted by distance to given coordinates."""
    # Assistance from https://stackoverflow.com/questions/19703975/django-sort-by-distance
    def nearby_locations(self, citylat, citylong, max_distance=None):
        """
        Return objects sorted by distance to specified coordinates
        which distance is less than max_distance given in kilometers
        """
        gcd_formula = "6371 * acos(cos(radians(%s)) * \
        cos(radians(citylat)) \
        * cos(radians(citylong) - radians(%s)) + \
        sin(radians(%s)) * sin(radians(citylat)))"
        
        distance_raw_sql = RawSQL(
            gcd_formula,
            (citylat, citylong, citylat)
        )
    
        if max_distance is not None:
            return self.annotate(distance=distance_raw_sql).filter(distance__lt=max_distance)
        else:
            return self.annotate(distance=distance_raw_sql)


class Profile(models.Model):
    """Represents a user profile with multiple fields and uses LocationManager to handle location-related queries."""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(max_length=500, default='', blank=False)
    APPROVAL = (
        ('TO BE APPROVED', 'To be approved'),
        ('APPROVED', 'Approved'),
        ('NOT APPROVED', 'Not approved')
    )
    
    RELATIONSHIP_STATUS = (
        ('', ''),
        ('NEVER MARRIED', 'Never Married'),
        ('DIVORCED', 'Divorced'),
        ('WIDOWED', 'Widowed'),
        ('SEPARATED', 'Separated')
    )
    
    
    GENDER = (
        ("", ""),
        ("MALE", "Male"),
        ("FEMALE", "Female"))

    gender = models.CharField(choices=GENDER, default="")
    
    relationship_status = models.CharField(choices=RELATIONSHIP_STATUS, default="NEVER MARRIED", blank=False)
    
    location = models.CharField(max_length=100, default='', blank=False)
    
    citylat = models.DecimalField(max_digits=9, decimal_places=6, default='-2.0180319')
    
    citylong = models.DecimalField(max_digits=9, decimal_places=6, default='52.5525525')
    
    birth_date = models.DateField(null=True, default='1990-01-01', blank=True)
    
    is_verified = models.CharField(choices=APPROVAL, default="TO BE APPROVED", blank=False, max_length=14)
    
    birth_date = models.DateField(null=True, default='1990-01-01', blank=True)
    
    objects = LocationManager()
    
    # Assistance from https://stackoverflow.com/questions/5056327/define-and-insert-age-in-django-template
    def age(self):
        """Method that calculates the user's age based on the date of birth."""
        return int((datetime.date.today() - self.birth_date).days / 365.25  )
    

# Assistance from https://stackoverflow.com/questions/2673647/enforce-unique-upload-file-names-using-django
def image_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/', filename)
    
    
class ProfileImage(models.Model):
    
    APPROVAL = (
        ('TO BE APPROVED', 'To be approved'),
        ('APPROVED', 'Approved'),
        ('NOT APPROVED', 'Not approved')
    )
    
    user = models.ForeignKey(User, default=None,  on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_filename, blank=True)
    is_verified = models.CharField(choices=APPROVAL, default="TO BE APPROVED", blank=False, max_length=14)
