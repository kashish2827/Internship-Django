from django.shortcuts import render,redirect
from .forms import UserForm



# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
        return render(request,'Core/register.html',{'form':form})