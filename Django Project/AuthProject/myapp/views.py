from django.shortcuts import render,redirect
from .forms import signupForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            messages.success(request,"Signup Successfully!")
            #return redirect('/')
        else:
            print(newuser.errors)
            messages.error(request,"Error! Something went wrong...")
    return render(request,'signup.html')