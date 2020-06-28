from django import forms
from first_app import models
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="")
    password = forms.CharField(widget= forms.PasswordInput())
    
    class Meta():
        model = models.User
        # fields = '__all__'
        fields = ['username','email','password']

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = models.UserProfileInfo
        fields = ['portfolio','picture']



