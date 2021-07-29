from django.urls import path
from . import views


urlpatterns = [
    #registration view
    path('register/', views.signup, name='register'),

    #activation urls
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('activate-success/', views.activate_success, name='activate-success'), 
    path('please-activate/', views.activate_success, name='please-activate'),  
    
]
