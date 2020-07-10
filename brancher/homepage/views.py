from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    print('hello')
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')
