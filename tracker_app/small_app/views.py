from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
#from .models import User
from django.contrib.auth.models import User
from .models import Expense, UserDetail
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required 
# Create your views here.

def landingPage(request):
    return render(request, 'landingpage.html')


def loginPage(request):
    return render(request, 'login.html')


def signUpPage(request): 
    return render(request, 'sign-up.html')


def profilePage(request):
    return render(request, 'profilepage.html')


def profileDisplay(request):
    return render(request, 'profiledisplay.html')

def addExpense(request):
    return render(request, 'addexpense.html')


def expenseHistory(request):
    return render(request, 'expensetable.html')


def analysisPage(request):
    return render(request, 'analysispage.html')


#def loginPage(request):
#    if request.method == 'POST':
#       username = request.POST['username']
#        password = request.POST['password']
#        user = authenticate(request, username=username, password=password)
#        if user is not None:
#            login(request, user)
#            return redirect('home')
#    return render(request, 'login.html')