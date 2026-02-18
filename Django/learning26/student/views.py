from django.shortcuts import render,redirect
from .forms import ServiceForm
from .models import Service

# Create your views here.
def Home(request):
    return render(request,'Student/home.html')
stu1=[
        {"rollno":1,"name":"Afrin","age":21,"std":"BE","city":"Bardoli","marks":30,"attendence":20},
        {"rollno":2,"name":"Kashish","age":20,"std":"BE","city":"Ahmedabad","marks":95,"attendence":25},
        {"rollno":3,"name":"Dhruv","age":21,"std":"BE","city":"Vadodara","marks":91,"attendence":18},
        {"rollno":4,"name":"Zeel","age":21,"std":"MBBS","city":"Patan","marks":94,"attendence":28}
        ]
def StuDetails(request):
    return render(request,'student/studetails.html',{"student":stu1}) 
def StuPass(request):
    return render(request,'student/stupass.html',{"student":stu1})
def StuAtt(request):
    return render(request,'student/stuatt.html',{"student":stu1})

def serviceList(request):
    services = Service.objects.all()
    return render(request,"student/serviceList.html",{"services":services})

def createservice(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("serviceList")
        else:
            return render(request,"student/createservice.html",{"form":form}) 
    else:
        form = ServiceForm()    
    return render(request,"student/createservice.html",{"form":form})

def deleteservice(request,serviceid):
    service = Service.objects.get(id=serviceid)
    service.delete()
    return redirect("serviceList")