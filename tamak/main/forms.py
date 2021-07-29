from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Comment

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label='Комментарий')
    class Meta:
        model = Comment
        fields = ['body']