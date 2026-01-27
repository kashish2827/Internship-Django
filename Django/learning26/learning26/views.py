from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("Hello!How are you?")
def AboutUs(request):
    return render(request,"aboutus.html")
def ContactUs(request):
    return render(request,"contactUs.html")
def Home(request):
    return render(request,"home.html")