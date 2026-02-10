from django.db import models

# Create your models here.
class User(models.Model):
    ROLE_CHOICES = (
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class Guest(models.Model):
    guest = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    booking_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.guest.username
    
class Host(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    host = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    earnings = models.FloatField(default=0.0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.host.username

class Admin(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.admin.username
    
class Property(models.Model):
    PROPERTY_TYPE_CHOICES = (
        ('villa', 'Villa'),
        ('apartment', 'Apartment'),
        ('homestay', 'Homestay'),
        ('farmhouse', 'Farmhouse'),
    )

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Maintenance'),
    )

    AVAILABILITY=(
        ('booked','Booked'),
        ('notbooked','Not Booked')
    )

    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=150)
    price = models.FloatField()
    amenities = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    availability = models.CharField(max_length=50, choices=AVAILABILITY)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
    
class Booking(models.Model):
    BOOKING_STATUS = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    )

    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    booking_status = models.CharField(max_length=15, choices=BOOKING_STATUS)
    total_amount = models.FloatField()

    def __str__(self):
        return f"Booking {self.id}"
    
class Payment(models.Model):
    PAYMENT_METHODS = (
        ('upi', 'UPI'),
        ('card', 'Card'),
        ('wallet', 'Wallet'),
        ('netbanking', 'NetBanking'),
    )

    PAYMENT_STATUS = (
        ('success', 'Success'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    )

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_method = models.CharField(max_length=15, choices=PAYMENT_METHODS)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id}"
    
class Review(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.id}"
    
class Wishlist(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.guest} - {self.property}"
    
class LocalExperience(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=150)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
