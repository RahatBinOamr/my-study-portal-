from django import forms
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ckeditor.fields import RichTextField

class NotesForm(forms.ModelForm):
  class Meta:
    model = Notes
    fields = ['title', 'description']
    widgets={
      'title':forms.TextInput(attrs={'class': 'form-control'}),
      'description':RichTextField()
    } 

class DateInput(forms.DateInput):
  input_type = 'date'
class homeWorkForm(forms.ModelForm):
  class Meta:
    model = HomeWork
    fields=['title','subject', 'description','due', 'is_finished']
    widgets={
        'title':forms.TextInput(attrs={'class': 'form-control'}),
        'subject': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'is_finished':forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'due':DateInput(),
    }


class DashboardForm(forms.Form):
  text=forms.CharField(max_length=250 , label='enter your search term :')

class TodoForm(forms.ModelForm):
  class Meta:
    model = Todo
    fields = ['title', 'is_finished']
    widgets={
      'title':forms.TextInput(attrs={'class': 'form-control'}),
      'is_finished':forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }

class userRegistrationForm(UserCreationForm):
  class Meta:
    model = User
    fields=['username','email','password1','password2']
    widgets={
      'username': forms.TextInput({'class': 'form-control'}),
      'email': forms.EmailInput({'class': 'form-control'}),
      'password1': forms.PasswordInput({'class': 'form-control'}),
      'password2': forms.PasswordInput({'class': 'form-control'}),
    }