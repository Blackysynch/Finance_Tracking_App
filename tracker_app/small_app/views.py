from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.contrib.auth.hashers import make_password
from .models import User,UserDetails
=======
from django.contrib.auth.hashers import make_password, check_password
#from .models import User
from django.contrib.auth.models import User
from .models import Expense, UserDetail
>>>>>>> e6c4076988d87143c6a9fb9c068cdb3deb90319f
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


 @login_required
def profilePage(request):
    if request.method == 'POST':
        user = request.user.id
        name = request.POST.get('name')
        email = request.user.email #request.POST.get('email')
        telephone = request.POST.get('tel')
        location = request.POST.get('location')
        country = request.POST.get('country')

        budgetmonthly = request.POST.get('monthly-budget')
        source_of_income = request.POST.get('income-source')
        other_sources = request.POST.get('additional-income')

        profile_picture = request.FILES.get('profile_picture')

        if not name:
            messages.error(request, 'a name  is required.')
        if not location:
            messages.error(request, 'a location  is required.')
        if not email:
            messages.error(request, 'a email  is required.')
        if not telephone:
            messages.error(request, 'a tel  is required.')
        if not country:
            messages.error(request, 'a country  is required.')

        if budgetmonthly:
            try:
                budgetmonthly = float(budgetmonthly)
                if budgetmonthly <= 0:
                    messages.error(request, 'Budget must be a positive number.')
            except ValueError:
                messages.error(request, 'Invalid budget format.')

        if not messages.get_messages(request):
            # Get the existing UserDetail instance or create a new one
            user_detail, created = UserDetail.objects.get_or_create(user_id=user)

            # Update the existing UserDetail instance
            if created:
                messages.success(request, 'Your profile was created.')
        
            user_detail.name = name
            user_detail.email = email
            user_detail.telephone = telephone
            user_detail.location = location
            user_detail.country = country
            user_detail.budgetmonthly = budgetmonthly
            user_detail.source_of_income = source_of_income
            user_detail.other_sources = other_sources

            # Save the profile picture
            if profile_picture:
                user_detail.profile_picture = profile_picture
            user_detail.save()


            return render(request, 'profilepage.html')

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