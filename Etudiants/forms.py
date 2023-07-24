from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class studentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name','email','phone','birthdate','filiere_id')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.PasswordInput(attrs={'class': 'form-control'}),
            'birthdate': forms.PasswordInput(attrs={'class': 'form-control'}),
            'filiere_id': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        #fields = '__all__'
        
class userForm(UserCreationForm):
    class Meta:
        model= User
        fields={
            'username',
            'email',
            'password1',
            'password2'
        }     
