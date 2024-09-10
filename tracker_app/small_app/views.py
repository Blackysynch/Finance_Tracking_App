<<<<<<< Updated upstream
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import render, redirect
from .models import User, Expense
from django.contrib.auth.models import User  # Make sure to import the User model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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
    def addExpense(request):
     if request.method == 'POST':
        # Retrieve data from the POST request
        user = request.user  # Assumes user is authenticated
        date = request.POST.get('date')
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        description = request.POST.get('description')

        # Validate the data (you can add more validation if needed)
        if not date or not category or not amount:
            return HttpResponse('Please fill in all required fields.')

        try:
            # Convert amount to Decimal type
            amount = float(amount)
        except ValueError:
            return HttpResponse('Invalid amount format.')

        # Save the data to the Expense model
        Expense.objects.create(
            user_id=user,
            date=date,
            category=category,
            amount=amount,
            description=description
        )

        return redirect('add_expense')  # Redirect to the same page after adding the expense

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
>>>>>>> Stashed changes
