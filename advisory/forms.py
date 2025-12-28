from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import FarmerProfile

class FarmerRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile = forms.CharField(max_length=10)
    location = forms.CharField(max_length=100)
    soil_type = forms.ChoiceField(choices=[
        ('Black', 'Black'), ('Red', 'Red'), ('Sandy', 'Sandy'),
        ('Alluvial', 'Alluvial'), ('Laterite', 'Laterite'), ('Loamy', 'Loamy')
    ])
    season = forms.ChoiceField(choices=[
        ('Kharif', 'Kharif'), ('Rabi', 'Rabi'), ('Zaid', 'Zaid')
    ])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',
                  'mobile', 'location', 'soil_type', 'season']
class FarmerProfileEditForm(forms.ModelForm):
    class Meta:
        model = FarmerProfile
        fields = ['mobile', 'location', 'soil_type', 'season']
