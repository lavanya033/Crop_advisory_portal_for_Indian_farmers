from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    soil_type = models.CharField(max_length=50)
    season = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username

