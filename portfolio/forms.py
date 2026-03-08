from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from . models import Project, Profile, ContactMessage


class RegisterForms(UserCreationForm):
    email = forms.EmailField()

    class Mete:
        model = User
        feilds = ["username", "email", "password", "password2"]


class ProjectForm(forms.ModelForm):
    model = Project
    fields = "__all__"



class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = "__all__"

class ProfileForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"