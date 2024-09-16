from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#users table
"""class User(models.Model):
    username = models.CharField(max_length= 50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, blank=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
"""


#user details
class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length= 50, null = True)
    email = models.EmailField(unique=True, null = True)
    telephone = models.CharField(max_length=20, null = True)
    location = models.CharField(max_length=20, null = True)
    country = models.CharField(max_length=20, null = True)
    budgetmonthly = models.DecimalField(max_digits=10, decimal_places=2, null = True)
    source_of_income = models.CharField(max_length=100, null = True)
    other_sources = models.CharField(max_length=100, null = True)
    
#expanse table
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    #year = models.IntegerField(null=True)


    def __str__(self):
        return f"{self.date} - {self.category} - {self.amount}"