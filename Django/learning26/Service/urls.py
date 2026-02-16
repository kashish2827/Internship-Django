from django.urls import path
from . import views

urlpatterns = [
    path('service/',views.Servicelist,name="servicelist"),
    path('serviceadd',views.AddService,name="addservice")
]
