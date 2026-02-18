from django.contrib import admin
from .models import Category, student,product,car,gymuser,gymuserprofile,gym,city,Trainer,Member,Service
 
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
admin.site.register(Service)
admin.site.register(Category)