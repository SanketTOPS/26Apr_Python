from django.shortcuts import render,redirect
from .forms import userForm
from .models import userInfo
# Create your views here.

def index(request):
    if request.method=='POST':
        newuser=userForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("User data has been saved!")
        else:
            print(newuser.errors)
    return render(request,'index.html')

def showdata(request):
    data=userInfo.objects.all()
    return render(request,'showdata.html',{'data':data})

def deletedata(request,id):
    stid=userInfo.objects.get(id=id)
    userInfo.delete(stid)
    return redirect('showdata')

def updatedata(request):
    return render(request,'updatedata.html')