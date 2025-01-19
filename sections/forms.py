
from django import forms
from django.contrib.auth.models import User
from .models import Section

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'users']
        widgets = {
            'users': forms.CheckboxSelectMultiple(),
        }
