from django.db import models

# Create your models here.
class employee(models.Model):
    gender = (
        ('male','Male'),
        ('female','Female')
    )
    empName = models.CharField(max_length=100)
    empSalary = models.IntegerField()
    empDesignation = models.CharField(max_length=100)
    empCity = models.CharField(max_length=50)
    empEmail = models.EmailField()
    empConatct = models.CharField(max_length=10)
    empAge = models.IntegerField()
    empJoiningDate = models.DateField(auto_now_add=True)
    empDepartment = models.CharField(max_length=100)
    empGender = models.CharField(max_length=50,choices=gender)

    class Meta:
        db_table="Employee"

    def __str__(self):
        return self.empName

class course(models.Model):
    cName = models.CharField(max_length=50)
    cFees = models.IntegerField()
    CDuration = models.IntegerField(default=6)
    class Meta:
        db_table="Course"
    def __str__(self):
        return self.cName

class gymuser(models.Model):
    userName = models.CharField(max_length=50)
    userEmail = models.EmailField(null=True)
    userPassword = models.CharField(max_length=100)
    userPhone = models.CharField(max_length=15, null=True)
    userAddress = models.TextField(null=True)

    class Meta:
        db_table="GYMMember"
    def __str__(self):
        return self.userName
    
class Toys(models.Model):
    toyname = models.CharField(max_length=100)
    toycategory = models.CharField(max_length=50)
    toyprice = models.IntegerField()
    discount = models.IntegerField()
    class Meta:
        db_table = "Toys"
    def __str__(self):
        return self.toyname
