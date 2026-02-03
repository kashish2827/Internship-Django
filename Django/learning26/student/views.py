from django.shortcuts import render

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