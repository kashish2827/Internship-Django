from django.contrib import admin
from .models import User,Guest,Host,Admin,Property,Booking,Payment,Review,Wishlist,LocalExperience

# Register your models here.
admin.site.register(User)
admin.site.register(Guest)
admin.site.register(Host)
admin.site.register(Admin)
admin.site.register(Property)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(Wishlist)
admin.site.register(LocalExperience)