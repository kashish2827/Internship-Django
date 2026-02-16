from django.urls import path
from . import views

urlpatterns = [
    path('emplist/',views.emplist,name="empList"),
    path('empfilter/',views.empFilter),
    path('createemployee/',views.createEmployee),
    path('createempform/',views.createEmployeewithform,name="createempForm"),
    path('course/',views.addCourse),
    path('gym/',views.gymMemberadd),
    path('toy/',views.toyAdd),
    path("deleteEmployee/<int:id>",views.DeleteEmp,name="deleteEmployee"),
    path("filterEmployee/",views.filterEmployee,name="filterEmployee"),
    path("sortEmployee/<int:id>",views.sortEmployee,name="sortEmployee"),
    path("updateemp/<int:id>",views.updateEmployee,name="updateemp")
]
