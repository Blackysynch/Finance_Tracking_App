from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import User, Expense
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse
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

@login_required
def addExpense(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        user = request.user.id # Assumes user is authenticated
        date = request.POST.get('date')
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        try:
            amount = float(amount)
            if amount <= 0:
                messages.error('Amount must be a positive number.')
        except ValueError:
            messages.error('Invalid amount format.')


        if not date:
            messages.error(request, 'Date is required.')
        if not category:
            messages.error(request, 'Category is required.')
        if not amount:
            messages.error(request,'Amount is required.')

        try:
            amount = float(amount)
            if amount <= 0:
                messages.error('Amount must be a positive number.')
        except ValueError:
            messages.error('Invalid amount format.')
        
        if description and len(description) > 255:
           messages.error('Description cannot exceed 255 characters.')


        # Save the data to the Expense model
        Expense.objects.create(
            user_id=request.user.id,
            date=date,
            category=category,
            amount=amount,
            description=description
        )

        return redirect('add-expense')  # Redirect to the same page after adding the expense

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