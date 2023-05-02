from django.contrib import admin
from django.urls import path, include
from mapapp import views

urlpatterns = [
    path('logout_user', views.logout_user, name="logout")
 ]
