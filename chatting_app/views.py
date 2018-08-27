from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm
from .models import Message
from django.db.models import Q
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

@login_required
def message(request):
	flag=False
	if request.method == 'POST':
		receiver_username=request.POST.get('receiver')
		r=User.objects.get(username=receiver_username)
		text=request.POST.get('message')
		sender=request.user
		Message.objects.create(text=text,sender=sender,receiver=r,read=False)
		flag=True
	s = request.user
	if flag==False:
		receiver_user_name=request.GET.get('name')
		r=User.objects.get(username=receiver_user_name)
	dialog=Message.objects.filter(Q(sender=s)|Q(sender=r))
	dialog=dialog.filter(Q(receiver=s)|Q(receiver=r)).order_by('created_date')
	return render(request,'message.html',{'convo':dialog,'sender':s,'receiver':r})

