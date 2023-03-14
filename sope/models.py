from django.db import models

# Create your models here.


class Employee(models.Model):
    EmpId = models.AutoField(primary_key = True)
    Name = models.TextField(max_length = 50, null = True, blank = True)
    DOB = models.DateField(null = True, blank = True)
    DOJ = models.DateField(null = True, blank = True)
    Department = models.TextField(max_length = 50, null = True, blank = True)
    Post = models.TextField(max_length = 50, null = True, blank = True)
    Address = models.TextField(max_length = 100, null = True, blank = True)
    City = models.TextField(max_length = 50, null = True, blank = True)
    Country = models.TextField(max_length = 50, null = True, blank = True)
    Zipcode = models.IntegerField(null = True, blank = True)
    State = models.TextField(max_length = 50, null = True, blank = True)
    Active = models.BooleanField(null = True, blank = True, default = False)
    Leave_count = models.IntegerField(default = 0,null = True, blank = True)
    On_leave = models.BooleanField(null = True, blank = True, default = False)
    
    