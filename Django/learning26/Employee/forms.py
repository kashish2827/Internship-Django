from django import forms
from .models import employee,course,gymuser,Toys
#this file create a form using django model it creates the fields according to the model

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = "__all__" #it creates all the fields that employee model have
    
class CourseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = "__all__"

class GymForm(forms.ModelForm):
    class Meta:
        model = gymuser
        fields = "__all__"

class ToyForm(forms.ModelForm):
    class Meta:
        model = Toys
        fields = "__all__"