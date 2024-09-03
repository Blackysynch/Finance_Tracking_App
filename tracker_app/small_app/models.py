from django.db import models

# Create your models here.

#users table
class User(models.Model):
    username = models.CharField(max_length= 50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


#user details
class UserDetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length= 50, unique=True)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    budgetmonthly = models.DecimalField(max_digits=10, decimal_places=2)
    source_of_income = models.CharField(max_length=100)
    other_sources = models.CharField(max_length=100)

#expanse table
class Expense(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
