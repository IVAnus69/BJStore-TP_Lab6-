from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.forms import ModelForm


class UserForm(UserCreationForm):
    profilePic = forms.ImageField(label='Изображение профиля', required=False)

    class Meta:
        model = User
        fields = ('username', 'profilePic', 'password1', 'password2')


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Имя")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())

# class UserImageForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('profilePic', )