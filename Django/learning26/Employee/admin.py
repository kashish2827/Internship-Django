from django.contrib import admin
from .models import employee,course,gymuser,Toys
# Register your models here.

admin.site.register(employee)
admin.site.register(course)
admin.site.register(gymuser)
admin.site.register(Toys)