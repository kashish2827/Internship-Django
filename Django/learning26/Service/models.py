from django.db import models

# Create your models here.
class Services(models.Model):
    sname = models.CharField(max_length=50)
    scategory = models.CharField(max_length=100)
    sprice = models.IntegerField()
    sdiscount = models.IntegerField()
    sdescription = models.CharField()
    class Meta:
        db_table = "SERVICE"
    def __str__(self):
        self.sname