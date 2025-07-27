from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomeUser

class CustomUserCreation(UserCreationForm):
    
    class Meta:
        model = CustomeUser
        fields = [ 'email','username', 'password1', 'password2']

class AuthenticationForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )