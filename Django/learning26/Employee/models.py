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

