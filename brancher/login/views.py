from django.shortcuts import render

# Create your views here.

def influencer (request):
    return render(request, 'login/influencer.html')

def company (request):
    return render(request, 'login/company.html')
