# from tkinter import Widget
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views



class CreateBlogForm(forms.ModelForm):
    blog_body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blogs
        fields = ['blog_body']

class LoginForm(forms.Form):
    remember_me = forms.BooleanField()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Email Address'}), label='Email Address')
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-3 required', 'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Password'}), label='Enter Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Confirm Password'}), label='Confirm Password')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class EditForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control mb-3'}), label='Email Address')
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-3 required'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Username'}))
    # password = None
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-4', 'type':'password', 'placeholder': 'Enter Password'}), label='Old Password')
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-4', 'type':'password', 'placeholder': 'Enter Password'}), label='Enter New Password', help_text="<ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>")
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'type':'password', 'placeholder': 'Enter Password'}), label='Confirm New Password')

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')