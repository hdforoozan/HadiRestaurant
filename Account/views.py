from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView,DetailView,ListView, CreateView
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib import messages


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(form.cleaned_data['password'])
			user.save()
			Profile.objects.create(user=user)
			return render(request, 'registration/signup_done.html', {'user':user})
	else:
		form = SignUpForm(request.POST)
	return render(request, 'registration/signup.html',{'form':form})

@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance= request.user, data= request.POST)
		profile_form = ProfileEditForm(instance= request.user.profile, data= request.POST, files=request.FILES)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Profile updated successfully')
			return redirect('dashboard')
		else:
			messages.error(request, 'Error updating your profile')

	else:
		user_form = UserEditForm(instance= request.user)
		profile_form = ProfileEditForm(instance= request.user.profile)

	return render(request, 'Account/edit.html',{'user_form':user_form, 'profile_form':profile_form})

@login_required
def dashboard(request):
	username = request.user.username
	email = request.user.email
	if email is None:
		email = 'blank'
	try:
		profile = Profile.objects.get(user=request.user)
	except Profile.DoesNotExist:
		profile = None
		
	return render(request, 'account/dashboard.html', {
	'username':username, 'email':email,'profile':profile,
	})
