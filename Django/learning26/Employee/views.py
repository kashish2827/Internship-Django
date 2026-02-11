from django.shortcuts import render,HttpResponse
from .models import employee
from .forms import EmployeeForm,CourseForm,GymForm,ToyForm
# Create your views here.

def emplist(request):
    emp = employee.objects.all().values()
    print(emp)
    return render(request,'employee/empList.html',{"emp":emp})

def empFilter(request):
    #select * from employee where empname=kashish
    empname = employee.objects.filter(empName="Kashish").values()
    print(empname)
    empcity = employee.objects.filter(empCity='Ahmedabad').values()
    print(empcity)
    empgender = employee.objects.filter(empGender='female').values()
    print(empgender)
    empcitydesi = employee.objects.filter(empSalary__gte=50000,empDesignation='Developer')
    print(empcitydesi)
    empage = employee.objects.filter(empAge__gt=20).values()
    print(empage)
    empsadedep = employee.objects.filter(empSalary__gte=50000,empDesignation='Developer')
    print(empsadedep)
    empsalary = employee.objects.order_by('empSalary').values()
    print(empsalary)
    empsalary1 = employee.objects.order_by('-empSalary').values()
    print(empsalary1)
    emppost = employee.objects.filter(empDepartment='Development')
    print(emppost)
    empdesi = employee.objects.filter(empDesignation='Developer')
    print(empdesi)
    emppost1 = employee.objects.filter(empDepartment__exact='development')
    emppost2 = employee.objects.filter(empDepartment__iexact='Development')
    print(emppost1)
    print(emppost2)
    empname1 = employee.objects.filter(empName__contains='A')
    empname2 = employee.objects.filter(empName__icontains='a')
    print(empname1)
    print(empname2)
    employee10 = employee.objects.filter(empName__startswith="k").values()
    employee11 = employee.objects.filter(empName__endswith="l").values()
    employee12 = employee.objects.filter(empName__istartswith="k").values()
    employee13 = employee.objects.filter(empName__iendswith="l").values()
    print(employee10)
    print(employee11)
    print(employee12)
    print(employee13)
    return render(request,'employee/empfilter.html',{"emp":empname})

def createEmployee(request):
    return HttpResponse("Employee Created....")

def createEmployeewithform(request):
    print(request.method)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        form.save()
        return HttpResponse("Employee created successfully....")
    else:
        form = EmployeeForm()
        return render(request,'employee/createempForm.html',{'form':form})
    
def addCourse(request):
    print(request.method)
    if request.method == "POST":
        form = CourseForm(request.POST)
        form.save()
        return HttpResponse("Course added successfully.....")
    else:
        form = CourseForm()
        return render(request,'employee/course.html',{'form':form})

def gymMemberadd(request):
    print(request.method)
    if request.method == "POST":
        form = GymForm(request.POST)
        form.save()
        return HttpResponse("GYM Member added successfully....")
    else:
        form=GymForm()
        return render(request,'employee/gymuser.html',{'form':form})
    
def toyAdd(request):
    print(request.method)
    if request.method == "POST":
        form = ToyForm(request.POST)
        form.save()
        return HttpResponse("Toys details added successfully... ")
    else:
        form=ToyForm()
        return render(request,'employee/toy.html',{'form':form})