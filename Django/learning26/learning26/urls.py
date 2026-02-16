"""
URL configuration for learning26 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from . import views 
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('aboutus/', views.AboutUs),
    path('contactUs/',views.ContactUs),
    path("",views.Home),
    path('movies/',views.Movies),
    path('news/',views.News),
    path('shows/',views.Shows),
    path('receipe/',views.Receipe),
    path('team/',views.Team),
    path('cars/',views.Cars),
    path("Student/",include("student.urls")),
    path("Emp/",include("Employee.urls")),
    path("Ser/",include("Service.urls"))
]   
