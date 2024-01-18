from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from myapp.models import student

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields=['username',"email",'password1','password2']
    

    


class Studentprofile(forms.ModelForm):
    class Meta:
        model= student
        fields= "__all__"