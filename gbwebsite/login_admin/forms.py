from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from .models import *
from django import forms


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        is_training_completed = False
        is_assessment_passed = False
        user.save()
        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': "aesthetic-windows-95-text-input", 'placeholder': 'Your username', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': "aesthetic-windows-95-text-input", 'placeholder': 'Password', 'id': 'password'}))
