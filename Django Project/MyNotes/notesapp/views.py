from django.shortcuts import render,redirect
from .forms import signupForm
from .models import userSignup
from django.contrib.auth import logout

# Create your views here.

def index(request):
    cuser=request.session.get('user')
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup Successfully!")
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':

            unm=request.POST['username']
            pas=request.POST['password']

            user=userSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfull!")
                request.session['user']=unm #create a session
                return redirect('notes')
            else:
                print("Error! Username or Password invalid...")
    return render(request,'index.html',{'cuser':cuser})

def notes(request):
    cuser=request.session.get('user')
    return render(request,'notes.html',{'cuser':cuser})

def profile(request):
    return render(request,'profile.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect('/')
