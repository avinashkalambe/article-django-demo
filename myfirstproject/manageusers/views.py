from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_as, logout
from author.models import Author
from django.core import serializers
from django.forms.models import model_to_dict

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            print('form is valid')
            f_username = form.cleaned_data.get('username')
            f_password = form.cleaned_data.get('password')
            f_email = form.cleaned_data.get('email')

            user = User.objects.create_user(username = f_username, password = f_password, email= f_email)
            
            if user != None:
                Author.objects.create(user=user)
                return redirect('login')
                
        else:
            print('not a valid form')
            return render(request, 'register.html',{'form' : form})

    form = RegisterForm()
    return render(request, 'register.html',{'form' : form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            f_username = form.cleaned_data.get('username')
            f_password = form.cleaned_data.get('password')
            user = authenticate(request, username= f_username, password= f_password)
            
            if user != None:
                login_as(request, user)
                
                try:                  
                    author = Author.objects.get(user=user)                    
                    request.session['author_id'] = author.id
                    request.session['author_name'] = author.user.username                    
                except Exception as e:
                    author = Author.objects.create(user=user)
                
                return redirect('/')
            else:
                return render(request, 'login.html', {'form' : form, 'error': 'username or passowrd is incorrect'})


    form = LoginForm()
    return render(request, 'login.html', {'form' : form})


def logout_user(request):
    logout(request)
    return redirect('/')