from django.shortcuts import render,redirect
from .forms import signupForm,updateForm
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
            
            userid=userSignup.objects.get(username=unm)
            print("Current User:",userid.id)

            user=userSignup.objects.filter(username=unm,password=pas)
            if user: #true
                print("Login Successfull!")
                request.session['user']=unm #create a session
                request.session['userid']=userid.id
                return redirect('notes')
            else:
                print("Error! Username or Password invalid...")
    return render(request,'index.html',{'cuser':cuser})

def notes(request):
    cuser=request.session.get('user')
    return render(request,'notes.html',{'cuser':cuser})

def profile(request):
    cuser=request.session.get('user')
    userid=request.session.get('userid')
    data=userSignup.objects.get(id=userid)
    if request.method=='POST':
        update=updateForm(request.POST,instance=data)
        if update.is_valid():
            update.save()
            print("Your profile has been updated!")
            return redirect('notes')
        else:
            print(update.errors)
    return render(request,'profile.html',{'cuser':cuser,'userid':data})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect('/')
