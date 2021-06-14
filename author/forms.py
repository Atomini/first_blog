from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):

    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        # help_texts = {
        #     'username': None,
        #     'password2': None,
        # }

        fields = ('username', 'password1', 'password2', "first_name", "email")

        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.TextInput(attrs={'class': 'form-control'}),
        }


