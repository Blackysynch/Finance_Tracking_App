from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
#from .models import User
from django.contrib.auth.models import User
from .models import Expense, UserDetail
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

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
    if request.method == 'POST':  
        # Accessing data from the POST request  
        username = request.POST.get('uname') 
        email = request.POST.get('email')  
        password = request.POST.get('password')  

        # Check for existing username and email  
        if User.objects.filter(username=username).exists():  
            return JsonResponse({'error': 'Username already exists.'})  
        if User.objects.filter(email=email).exists():  
            return JsonResponse({'error': 'Email already exists.'})  

        # Create new user with hashed password  
        hashed_password = make_password(password)  # Hashes the password for security  
        new_user = User(username=username, email=email, password=hashed_password)  
        new_user.save()  
        
        print(f"account details are {username} {email} {password}, {hashed_password}")
        return JsonResponse({'message': 'User created successfully'}) 
    # Render the signup page if not a POST request 
    return render(request, 'sign-up.html')
# After successful user creation  
    return redirect('login-page')



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

@login_required
def profileDisplay(request):
    user_detail = UserDetail.objects.get(user_id=request.user.id)
    return render(request, 'profiledisplay.html', {'user_detail': user_detail})


@login_required
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




@login_required
def expenseHistory(request):
    username = request.user.username
    user_expenses = Expense.objects.filter(user=request.user)

    # Print expense details
    for expense in user_expenses:
        print(f"Date: {expense.date}, Category: {expense.category}, Amoun:t {expense.amount}, Description: {expense.description}")

    return render(request, 'expensetable.html', {'expenses': user_expenses})



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