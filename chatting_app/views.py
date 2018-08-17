from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm
from .models import Dialog
from .models import Message
from django.http import HttpResponse, JsonResponse
from datetime import datetime
@login_required
def home(request):
	s = request.user
	user_objects=User.objects.exclude(username=s.username)
	return render(request,'home.html',{'home':'active','sender':s,'users_except':user_objects})

def signup(request):
	if request.method=='POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user=authenticate(username = username, password = password)
			login(request,user)
			return redirect('home')
	else:
		form = SignupForm()
	return render(request,'signup.html',{'form':form})



