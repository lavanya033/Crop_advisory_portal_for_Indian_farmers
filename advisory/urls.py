# advisory/urls.py
from django.urls import path
from . import views 
from .views import register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/',views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('recommend/', views.crop_recommendation, name='crop_recommend'),
    path('government/', views.government_schemes, name='govern_schemes'),
    path('weather/', views.weather_view, name='weather'),
    path('chatbot/', views.chatbot_view, name='chatbot'),

]

