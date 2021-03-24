from django.db import models

# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    uname = models.CharField(max_length=30)
    psd = models.CharField(max_length=30)

    def __str__(self):
        return self.fname
class Mark(models.Model):
    mid=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    m1=models.FloatField(null=True)
    m2=models.FloatField(null=True)
    m3=models.FloatField(null=True)