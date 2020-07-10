from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('about/', views.about, name='homepage-about'),
    path('services/', views.services, name='homepage-services'),
    path('companies/', views.about, name='homepage-companies'),
    path('influencer/', views.about, name='homepage-influencer'),
]
