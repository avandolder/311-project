from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import UserCreationForm


def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/finder')
	else:
		form = UserCreationForm()
	return render(request, 'finder/signup.html', {'form':form})

def index(request):
    return render(request, 'finder/index.html', {})

def logout(request):
	django_logout(request)
	return redirect('/login')

def profile(request):
	return render(request, 'finder/profile.html')

def search(request):
	if request.method == 'GET':
		search_query = request.GET.get('search_box', None)
		#query course database
	return render(request, 'finder/search.html')

def faqs(request):
	return render(request, 'finder/faqs.html')

def paths(request):
	#return users saved paths
	return render(request, 'finder/paths.html')