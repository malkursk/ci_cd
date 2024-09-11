
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('accounts/profile/', views.profile, name = 'profile'),
    path('social/', include('social_django.urls', namespace = 'social_auth')),
]
