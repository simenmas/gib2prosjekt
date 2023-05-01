from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mapapp import models
class RegisterNewUser(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]

class PointForm(forms.ModelForm):
    class Meta:
        model = models.Point
        exclude = []