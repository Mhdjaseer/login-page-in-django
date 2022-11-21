from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import cache_control
# Create your views here.

# home page
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    return render(request,"home.html")

# register
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    if request.method == 'POST':
        firstname=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User taken')
                return redirect('register')
    
            elif User.objects.filter(email=email).exists() :
                messages.info(request,'email is taken')
                
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=last_name)
                user.save()
                print('uuser is created')
                return redirect('login_view')
                
        else:
            messages.info(request,'user password is not matched ')
            return redirect('register')
        return redirect('/')
    else:
        
        return render(request,'registration/signup.html')
    
# login  
@cache_control(no_cache=True, must_revalidate=True)
def login_view(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'user not fount')
            return redirect('login_view')
    else:
        return render(request,'registration/login.html')
    

# logout
def logout_view(request):
    logout(request)
    return redirect('/')