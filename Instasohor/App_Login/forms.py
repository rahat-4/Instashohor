from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from .models import UserProfile

class SignupForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={"placeholder":"Email"}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder":"Password Confirmation"}))
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder":"Username"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    class Meta:
        model = User
        fields = '__all___'

class EditProfileForm(forms.ModelForm):
    f_name = forms.CharField(label="" , required=False, widget=forms.TextInput(attrs={"placeholder":"First name", "blank":True}))
    l_name = forms.CharField(label="", required=False,widget=forms.TextInput(attrs={"placeholder":"Last name"}))
    dob = forms.DateField(label="Date of Birth", required=False,widget=forms.TextInput(attrs={"type":"date"}))
    about = forms.CharField(label="", required=False, widget=forms.Textarea(attrs={"placeholder":"Say something about yourself"}))
    profile_pic = forms.ImageField(label="Profile Picture", required=False)
    facebook_url = forms.URLField(label="", required=False, widget=forms.TextInput(attrs={"placeholder":"Facebook link"}))
    website_url = forms.URLField(label="", required=False, widget=forms.TextInput(attrs={"placeholder":"Website link"}))
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'dob', 'f_name', 'l_name', 'about', 'website_url', 'facebook_url']
        # fields = '__all__'