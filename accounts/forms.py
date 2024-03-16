from django import forms
from django.contrib.auth.models import User

class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


