from django.shortcuts import render,HttpResponse,redirect
from .forms import ServiceForm
from .models import Services

# Create your views here.
def AddService(request):
    print(request.method)
    if request.method == "POST":
        form = ServiceForm(request.POST)
        form.save()
        return redirect("servicelist")
    else:
        form = ServiceForm()
        return render(request,'Service/serviceadd.html',{'form':form})

def Servicelist(request):
    service = Services.objects.all().order_by('id').values()
    print(service)
    return render(request,'Service/servicelist.html',{'service':service})