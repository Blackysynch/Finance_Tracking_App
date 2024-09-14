from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name='landing-page'),
    path('login/', views.loginPage, name='login-page'),
    path('signup/', views.signUpPage, name='sign-up'),
    path('profilepage/', views.profilePage, name='profile-page'),
    path('profile/', views.profileDisplay, name='profile-display'),
    path('addexpense/', views.addExpense, name='add-expense'),
    path('expensehistory/', views.expenseHistory, name='expense-history'),
    path('analysis/', views.analysisPage, name='analysis-page'),
    path('logout/', views.logOut, name='log-out'),
]
