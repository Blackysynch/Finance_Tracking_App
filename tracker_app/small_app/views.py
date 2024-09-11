"""
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
"""
from django.shortcuts import render, redirect  
from django.http import JsonResponse  
from django.contrib.auth.hashers import make_password  
from django.contrib import messages  
from .models import User

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




#def signUpPage(request):
    
    """
    if request.method == 'POST':  
        username = request.POST['uname']  
        email = request.POST['email']  
        password = request.POST['password']  

        # Check if username or email already exists  
        if User.objects.filter(username=username).exists():  
            messages.error(request, 'Username already exists.')  
            return redirect('sign-up')  
        if User.objects.filter(email=email).exists():  
            messages.error(request, 'Email already exists.')  
            return redirect('sign-up')  

        # Create new user with hashed password  
        hashed_password = make_password(password)  
        new_user = User(username=username, email=email, password=hashed_password)  
        new_user.save()  

        messages.success(request, 'Account created successfully! You can now log in.')  
        return redirect('login-page')
    
    
    
    if request.method == 'POST':
        if request.content_type == 'application/x-www-form-urlencoded':
        
            username = data['username']
            email = data['email']
            password = data['password']
        
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error':'username exists already'})
        
            user = User.objects.create_user(username=username, email=email,password=password)
            return JsonResponse({'message': 'User created succesfully'})
        else:
            print(f"Unexpecte content type: {request.content_type}")
    else:
        return render(request, 'sign-up.html')
"""

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



def signUpPage(request):  
    if request.method == 'POST':  
        # Accessing data directly from the POST request  
        username = request.POST.get('uname')  # Change these keys to match your form input names  
        email = request.POST.get('email')  
        password = request.POST.get('password')  

        # Check for existing username and email  
        if User.objects.filter(username=username).exists():  
            return JsonResponse({'error': 'Username already exists.'})  
        if User.objects.filter(email=email).exists():  
            return JsonResponse({'error': 'Email already exists.'})  

        # Create new user with hashed password  
        hashed_password = make_password(password)  # Hash the password for security  
        new_user = User(username=username, email=email, password=hashed_password)  
        new_user.save()  
        
        return JsonResponse({'message': 'User created successfully'}) 
    # Render the signup page if not a POST request 
    return render(request, 'sign-up.html')
# After successful user creation  
    return redirect('login-page')  # Redirect to the login page after successful registration
        #return JsonResponse({"status": "success", "message": "User registered successfully!"})  
    #return JsonResponse({"status": "fail", "message": "Invalid request."})  

        #return JsonResponse({'message': 'User created successfully'})  
    
    # Render the signup page if not a POST request  
    #return render(request, 'sign-up.html')