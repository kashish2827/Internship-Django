from django.contrib import admin
from .models import student,product,car,gymuser,gymuserprofile,gym,city,Trainer,Member
 
# Register your models here.

admin.site.register(student)
admin.site.register(product)
admin.site.register(car)
admin.site.register(gymuser)
admin.site.register(gymuserprofile)
admin.site.register(city)
admin.site.register(gym)
admin.site.register(Trainer)
admin.site.register(Member)