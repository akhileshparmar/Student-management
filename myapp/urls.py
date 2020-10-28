"""my app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.login, name='login'),
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout"),	
    path('home', views.home, name="home"),
    path("lists/<str:str>", views.lists, name="lists"),
    path("profile/<int:Scholar_no>", views.profile, name="profile"),
    path('search', views.search, name="search")
    #path("lists/<int:no>", views.lists, name="lists"),
	#path("result/<int:Scholar_no>", views.result, name="result")

    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)