from django.shortcuts import render,redirect
from .forms import userForm,updateData
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

def updatedata(request,id):
    stid=userInfo.objects.get(id=id)
    if request.method=='POST':
        updateform=updateData(request.POST,instance=stid)
        if updateform.is_valid():
            updateform.save()
            print("Your data has been updated!")
            return redirect('showdata')
        else:
            print(updateform.errors)
    return render(request,'updatedata.html',{'stid':stid})