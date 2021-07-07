from django import forms
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Username"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Last Name"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter Password"}), label="Type Password", validators=[MinLengthValidator(8)])
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm password"}), label="Confirm password", validators=[MinLengthValidator(8)])
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter Password"}), label="Type Password", validators=[MinLengthValidator(8)])
