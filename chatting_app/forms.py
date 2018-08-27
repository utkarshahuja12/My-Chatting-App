from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Message
class SignupForm(UserCreationForm):
	first_name=forms.CharField(max_length=45,required=True,help_text='Mandatory')
	last_name=forms.CharField(max_length=45,required=True,help_text='Mandatory')
	email=forms.EmailField(max_length=255,required=True, help_text='Not a valid email address')
	class Meta:
		model=User
		fields=('username','first_name','last_name','email','password1','password2',)

class NewMessage(forms.ModelForm):
	class Meta:
		model =Message
		fields=('text',)