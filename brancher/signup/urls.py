from django.urls import path
from . import views


urlpatterns = [
    path('', views.influencer, name='signup'),
    path('influencer/', views.influencer, name='influencer-signup'),
    path('company/', views.company, name='company-signup'),
]
