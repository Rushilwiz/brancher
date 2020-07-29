from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User, Group

from .forms import InfluencerRegisterForm, CompanyRegisterForm

# Create your views here.

def influencerlogin (request):
    return render(request, 'users/influencerlogin.html')

def companylogin (request):
    return render(request, 'users/companylogin.html')

def influencersignup (request):
    if request.method == 'POST':
        form = InfluencerRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            influencer_group, created = Group.objects.get_or_create(name='Influencer')
            new_user.groups.add(influencer_group)

            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            return redirect('app')
    else:
        form = InfluencerRegisterForm()
    return render(request, 'users/influencersignup.html', {'form': form})

def companysignup (request):
    if request.method == 'POST':
        form = CompanyRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            company_group, created = Group.objects.get_or_create(name='Company')
            new_user.groups.add(company_group)

            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            return redirect('app')
    else:
        form = CompanyRegisterForm()
    return render(request, 'users/companysignup.html', {'form': form})

def logout (request):
    auth_logout(request)
    return redirect('/')
