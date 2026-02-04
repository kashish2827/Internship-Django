from django.db import models

# Create your models here.
class student(models.Model):
    studentName=models.CharField(max_length=50)
    studentAge=models.IntegerField()
    studentCity=models.CharField(max_length=50)
    studentEmail=models.EmailField(null=True)

    class Meta:
        db_table="student"

class product(models.Model):
    productName = models.CharField(max_length=70)
    productPrice = models.IntegerField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=50,null=True)
    productStatus = models.BooleanField(default=True)
    productDescription = models.TextField(null=True)
    class Meta:
        db_table="Product"

class car(models.Model):
    carName = models.CharField(max_length=60)
    carModelYear = models.IntegerField(max_length=4)
    carDescription = models.CharField(max_length=100)
    carFeatures = models.TextField(null=True)
    carBuyDate = models.DateField(null=True)
    carOwner = models.CharField(null= True, max_length=50)
    carPrice = models.IntegerField(null=True)

    class Meta:
        db_table="Car"
