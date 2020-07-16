from django.urls import path
from . import views


urlpatterns = [
    path('', views.influencer, name='login'),
    path('influencer/', views.influencer, name='influencer-login'),
    path('company/', views.company, name='company-login'),
]
