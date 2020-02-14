from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# After importing auth please do migrate.

def signup(request):
	if request.method == 'POST':
		# User has info and wants an account i.e Post request means need an account
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accounts/signup.html', {'error':'User already exists!'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
				auth.login(request, user)
				return redirect('home')
		else:
			return render(request, 'accounts/signup.html', {'error':'Passwords must match!'})

	else:
		# User wants to enter Info
		return render(request, 'accounts/signup.html')


def login(request):
	if request.method == 'POST':
		# Get request means user has account just wants to login.
		user=auth.authenticate(username = request.POST['username'], password = request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else:
			return render(request, 'accounts/login.html', {'error':'username or password is incorrect!'})
	else:
		return render(request, 'accounts/login.html')


def logout(request):
	#when someone logout then we want them to return to homepage. 
	if request.method=='POST':
		auth.logout(request)
		return redirect('home') 