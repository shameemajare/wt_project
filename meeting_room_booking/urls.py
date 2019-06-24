"""booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'meeting_room_booking'

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('tosignup/',views.tosignup,name="tosignup"),
    path('test/',views.test,name="test"),
    path('toBook/',views.toBook,name="toBook"),
    path('toHome/',views.toHome,name="toHome"),
    path('toCancel/',views.toCancel,name="toCancel"),
    path('confirm/',views.confirm,name="confirm"),
    path('toFeed/',views.toFeed,name="toFeed"),
    path('cancelbook/',views.cancelbook,name="cancelbook"),
    path('myBook/',views.myBook,name="myBook"),
    path('toAbout/', views.toAbout, name="toAbout"),
path('toContact/', views.toContact, name="toContact"),
path('toFAQ/', views.toFAQ, name="toFAQ"),
path('feedback/', views.tofeedback, name="tofeedback"),
    path('check_avail/',views.check_avail,name='check_avail')
    #path('feedback/',views.feedback,name="feedback")


]
