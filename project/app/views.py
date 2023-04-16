from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from .models import Money, VerificationBadge

# Create your views here.
def home(request):
    moneys = Money.objects.filter(user=request.user)
    return render(request, 'home.html', {'moneys' : moneys})

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect(register)
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Pubg ID already used')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                return redirect('login_user')
            
    else:
        return render(request, 'registration.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')
        
    else:
        return render(request, 'login.html')
    
def logout_user(request):
    auth.logout(request)
    return redirect('login_user')

def profile(request):
    moneys = Money.objects.filter(user=request.user)
    verify = VerificationBadge.objects.filter(user=request.user)
    return render(request, 'profile.html', {'moneys' : moneys, 'verify' : verify})

def add_pay(request):
    return render(request, 'add_payment.html')

def ucpubg(request):
    moneys = Money.objects.filter(user=request.user)
    return render(request, 'ucpubg.html', {'moneys' : moneys})

def firebase(request):
    moneys = Money.objects.filter(user=request.user)
    verify = VerificationBadge.objects.filter(user=request.user)
    return render(request, 'firebase.html', {'moneys' : moneys, 'verify' : verify})

def instagram(request):
    moneys = Money.objects.filter(user=request.user)
    verify = VerificationBadge.objects.filter(user=request.user)
    return render(request, 'instagram.html', {'moneys' : moneys, 'verify' : verify})