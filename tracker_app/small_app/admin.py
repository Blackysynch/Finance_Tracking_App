from django.contrib import admin
from .models import Expense, UserDetail #bring Users, Expenses

# Register your models here.
#admin.site.register(User)
admin.site.register(Expense)
admin.site.register(UserDetail)