from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse
# Create your views here.

def landingPage(request):
    return render(request, 'landingpage.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')   


        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,   
 user)
            # Successful authentication
            return redirect(reverse(profilePage))  # Replace with your desired success page
        else:
            # Authentication failed
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'login.html')


def signUpPage(request):
    return render(request, 'sign-up.html')


def profilePage(request):
    return render(request, 'profilepage.html')


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