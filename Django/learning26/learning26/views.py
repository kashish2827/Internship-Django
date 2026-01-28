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
def Movies(request):
    return render(request,"movies.html")
def News(request):
    return render(request,"news.html")
def Shows(request):
    return render(request,"shows.html")
def Receipe(request):
    ingredient=['Bread','Chesse','Ketchup','Veggies','Butter']
    data={"name":"Sandwich","time":30,"Ingredients":ingredient}
    return render(request,"receipe.html",data)
def Team(request):
    teamlist=['Smriti mandana','Radha Yadav','Arundhati Reddy','Richa Gosh','Ellyse Perry',
              'Shreyanka Pati','Lauren Bell','Georgia Voll','Gautami Naik','Linsey Smith',
              'Pooja Vastrakar','Grace Harris','Nadine de Klerk']
    data={
        "tname":"RCB",
        "cap":"Smriti Mandana",
        "trophy":1,
        "teamlist":teamlist
    }
    return render(request,'team.html',data)