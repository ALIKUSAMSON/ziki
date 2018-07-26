from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, SignUpForm
from django.http import HttpResponse, HttpResponseRedirect, response
from .models import Account
from django.contrib.auth.hashers import check_password, make_password
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('home')
			else:
				messages.info(request,'Your password or username was wrong')
				return redirect(reverse('login'))
	else:
		return render(request, 'accounts/login.html', context={'form':form})



def signup_view(request):
	form = SignUpForm()
	registered = False
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			confirm = form.cleaned_data['confirm']
			check = Account.objects.filter(username=username)
			if password == confirm:
				if check:
					return redirect(reverse('signup'))
				else:
					user = Account.objects.create(username=username,email=email,password=make_password(password,salt=None,hasher='default'))
					user.save()
					registered =True
					return redirect(reverse('login'))
		else:
			return redirect(reverse('signup'))
	else:
		return render(request, 'accounts/signup.html' ,context={'form':form, 'registered':registered})

def logout_view(request):
	logout(request)
	return redirect('home')

#@login_required
#def my_view(request):
#	if not request.user.is_authenticated:
#		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))