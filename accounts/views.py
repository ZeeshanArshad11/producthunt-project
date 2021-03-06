from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2'] :
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'User already exist!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                messages.success(request, "Your account created Successfully")
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Password doesnot match!'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'] , password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are successfully login")
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'UserName or Password is incorrect!'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    # redirect to the homepage
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You are successfully logout")
        return redirect('home')
