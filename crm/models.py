from django.db import models

# Create your models here.

class Employees(models.Model):
    Name=models.CharField(max_length=200)
    Department=models.CharField(max_length=200)
    Salary=models.PositiveIntegerField()
    Email=models.EmailField(unique=True)
    Contact=models.CharField(null=True, max_length=20)
    Age=models.PositiveIntegerField() 
    Profile_pic=models.ImageField(upload_to="images",null=True,blank=True)
    DOB=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.Name
    

    