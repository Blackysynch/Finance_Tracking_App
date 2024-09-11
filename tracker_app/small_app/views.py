from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse
import os


=======
from django.contrib.auth.hashers import make_password, check_password
#from .models import User
from django.contrib.auth.models import User
from .models import Expense, UserDetail
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required 
>>>>>>> e6c4076988d87143c6a9fb9c068cdb3deb90319f
# Create your views here.

def landingPage(request):
    return render(request, 'landingpage.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('Name')
        password = request.POST.get('password')


        print(f" {username}, {password}")

        if not username or not password:
            messages.error(request, 'username and password are required')
            return render(request, 'login.html')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:

                login(request, user)
                messages.success(request, 'You have successfully logged in')
                return redirect('profile-page')
            else:
                messages.error(request, 'Account is inactive')
                return render(request, 'login.html')
        else:

            print(f"User is {user} does not exist")
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')

    return render(request,'login.html')




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