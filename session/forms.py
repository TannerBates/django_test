from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Post
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from django import forms
from django.db import models

class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise forms.ValidationError('Username must be longer than 5 characters')
        elif len(username) > 50:
            raise forms.ValidationError('Username must be less than 50 characters')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email = email).exists():
            raise forms.ValidationError('This email is already registered')
        return email


    class Meta:
        model = CustomUser
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text = "Usernames must be no more than 50 characters"

        for fieldname in ['password1']:
            self.fields[fieldname].help_text = "Password cannot contain any personal information"

        for fieldname in ['password2']:
            self.fields[fieldname].help_text = "Passwords must match"

        CustomUser._meta.get_field('email')._unique = True
        
        

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')



class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')