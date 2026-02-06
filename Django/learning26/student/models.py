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
    carModelYear = models.IntegerField()
    carDescription = models.CharField(max_length=100)
    carFeatures = models.TextField(null=True)
    carBuyDate = models.DateField(null=True)
    carOwner = models.CharField(null= True, max_length=50)
    carPrice = models.IntegerField(null=True)

    class Meta:
        db_table="Car"

class gymuser(models.Model):
    userName = models.CharField(max_length=50)
    userEmail = models.EmailField(null=True)
    userPassword = models.CharField(max_length=100)
    userPhone = models.CharField(max_length=15, null=True)
    userAddress = models.TextField(null=True)

    class Meta:
        db_table="GYMUser"
    def __str__(self):
        return self.userName

class gymuserprofile(models.Model):
    bodytype = (('Ectomorph', 'Ectomorph'),
                ('Mesomorph', 'Mesomorph'),
                ('Endomorph', 'Endomorph'))
    time = (('Morning', 'Morning'),
            ('Afternoon', 'Afternoon'),
            ('Evening', 'Evening'))
    userId = models.OneToOneField(gymuser, on_delete=models.CASCADE)
    bodytype = models.CharField(max_length=50,choices=bodytype)
    dateOfBirth = models.DateField(null=True)
    workouttime = models.CharField(max_length=50,choices=time)

    class Meta:
        db_table="GYMUserProfile"
    def __str__(self):
        return self.userId.userName
    
class city(models.Model):
    cityName=models.CharField(max_length=50)

    class Meta:
        db_table="GYM City"
    
    def __str__(self):
        return self.cityName
    
class gym(models.Model):
    gymName = models.CharField(max_length=100)
    gymLocation = models.CharField(max_length=100)
    gymContact = models.CharField(max_length=15)
    gymEmail = models.EmailField(null=True)
    gymDescription = models.TextField(null=True)
    cityID=models.ForeignKey(city,on_delete=models.CASCADE)

    class Meta:
        db_table="GYM"

    def __str__(self):
        return self.gymName
   
class Trainer(models.Model):
    TrainerName = models.CharField(max_length=50)
    TrainerCity = models.CharField(max_length=50)
    TrainerContact = models.CharField(max_length=10)
    TrainerEmail = models.EmailField()
    cityId = models.ForeignKey(city,on_delete=models.CASCADE)

    class Meta:
        db_table="Trainer"
    def __str__(self):
        return self.TrainerName
    
class Member(models.Model):
    MemberName = models.CharField(max_length=50)
    MemberCity = models.CharField(max_length=50)
    MemberEmail = models.EmailField()
    MemberContact = models.CharField(max_length=10)
    MemberID = models.ForeignKey(Trainer,on_delete=models.CASCADE)
    #cityId = models.ForeignKey(city,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table="Member"
    def __str__(self):
            return self.MemberName
        