from django.contrib.auth.models import User
from django import forms


class registerform(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password","first_name","last_name","email"]



