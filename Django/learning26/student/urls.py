from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.Home),
    path('details/',views.StuDetails),
    path('pass/',views.StuPass),
    path('attendence/',views.StuAtt),
    path('services/',views.serviceList,name="serviceList"),
    path('createService/',views.createservice,name="createService"),
    path('deleteService/<int:serviceid>/',views.deleteservice,name="deleteService")
]
