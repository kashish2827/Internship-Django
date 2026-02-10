from django.urls import path
from . import views

urlpatterns = [
    path('emplist/',views.emplist),
    path('empfilter/',views.empFilter)
]
