"""Practice1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first_app import views

app_name = "first_app"

urlpatterns = [
    path(route='',view=views.index,name='Index'),
    path(route='topictable/',view=views.topicTable,name='topicTable'),
    path(route='forms/',view=views.ViewForm,name='FormPage'),
    path(route='register/',view=views.NewUser,name='NewUser'),
    path(route='login/',view=views.user_login,name='user_login'),
    path(route='logout/',view=views.user_logout,name='user_logout'),
    
]
