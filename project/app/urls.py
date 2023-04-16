from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name="register"),
    path('login/', views.login_user, name="login_user"),
    path('home/', views.home, name="home"),
    path('logout/', views.logout_user, name="logout_user"),
    path('profile/', views.profile, name="profile"),
    path('add_pay/', views.add_pay, name="add_pay"),
    path('ucpubg/', views.ucpubg, name="ucpubg"),
    path('firebase/', views.firebase, name="firebase"),
    path('instagram/', views.instagram, name="instagram"),
]