from django.shortcuts import render,redirect
from .forms import signupForm
from django.contrib import messages
from .models import userSignup
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=userSignup.objects.filter(username=unm, password=pas)
        if user: #true
            print("Login Successfully!")
            request.session['user']=unm #create a session
            messages.success(request,"Login Successfully!")

            return redirect('home')
        else:
            print("Error! Login fail....Try again")
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            messages.success(request,"Signup Successfully!")
            return redirect('/')
        else:
            print(newuser.errors)
            messages.error(request,"Error! Something went wrong...")
    return render(request,'signup.html')

def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')
