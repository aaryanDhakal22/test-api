from django.db import models

# Create your models here.

class StudentModel(models.Model):
    unid = models.CharField(max_length=50,default=0,primary_key=True )
    name = models.CharField(max_length=100,default='')
    phone = models.BigIntegerField(default=0)
    gender = models.CharField(max_length=10,default='')
    father = models.CharField(max_length=40,default='')
    mother = models.CharField(max_length=40,default='')
    address = models.CharField(max_length=100,default='')
    group=models.CharField(max_length=5,default='')
    age=models.IntegerField(default=0)
    dob = models.CharField(max_length=12,default='')
    speechTherapy = models.IntegerField(default=0 )
    therapy= models.IntegerField(default= 0)
    transportation = models.IntegerField(default=0 )
    admissionCharge = models.IntegerField(default=0 )
    monthlyCharge = models.IntegerField(default=0 )
    snacks = models.IntegerField(default=0 )
    isAdmission = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class TransactionModel(models.Model):
    studentunid= models.CharField(max_length=50,default=0,primary_key=True )
    date = models.CharField(max_length=12,default='')
    paidAmount = models.IntegerField(default=0)
    forMonth = models.CharField(max_length=20)
    speechTherapy = models.IntegerField(default=0 )
    therapy= models.IntegerField(default= 0)
    transportation = models.IntegerField(default=0 )
    admissionCharge = models.IntegerField(default=0 )
    monthlyCharge = models.IntegerField(default=0 )
    snacks = models.IntegerField(default=0 )


    def __str__(self):
        return str(self.date)


