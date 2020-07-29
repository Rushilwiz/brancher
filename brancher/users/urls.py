from django.urls import path
from . import views


urlpatterns = [
    path('login/company/', views.companylogin),
    path('login/influencer/', views.influencerlogin, name='login'),
    path('signup/company/', views.companysignup),
    path('signup/influencer/', views.influencersignup, name='signup'),
    path('logout/', views.logout, name='logout')
]
