from django import forms
from .models import Candidate
from django.contrib.auth.admin import User


class CandiForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = '__all__'


class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class Registration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]

