from django.urls import path
from . import views

urlpatterns = [
    path('emplist/',views.emplist),
    path('empfilter/',views.empFilter),
    path('createemployee/',views.createEmployee),
    path('createempform/',views.createEmployeewithform),
    path('course/',views.addCourse),
    path('gym/',views.gymMemberadd),
    path('toy/',views.toyAdd)
]
