from django.urls import path
from . import views

urlpatterns = [
    path('service/',views.Servicelist,name="servicelist"),
    path('serviceadd',views.AddService,name="addservice"),
    path('updateservice/<int:id>',views.updateservice,name='updateservice'),
    path('deleteservice/<int:id>',views.deleteservice,name='deleteservice')
]
