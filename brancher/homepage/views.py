from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')

def services(request):
    return render(request, 'homepage/services.html')

def companies(request):
    return render(request, 'homepage/companies.html')

def influencer(request):
    return render(request, 'homepage/influencerw.html')
