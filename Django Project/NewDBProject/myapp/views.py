from django.shortcuts import render
from .forms import userdataForm
from .models import userinfo

# Create your views here.

def index(request):
    if request.method=='POST':
        newuser=userdataForm(request.POST)
        if newuser.is_valid(): #true
            newuser.save()
            print("Your data has been saved!")
        else:
            print(newuser.errors)
    return render(request,'index.html')

def showdata(request):
    data=userinfo.objects.all()
    return render(request,'showdata.html',{'data':data})