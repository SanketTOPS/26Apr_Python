from django.shortcuts import render,redirect
from .forms import signupForm,updateForm,notesForm,callbackForm
from .models import userSignup
from django.contrib.auth import logout
from django.core.mail import send_mail
from MyNotes import settings
import requests
import random

# Create your views here.
status=False
def index(request):
    global status
    cuser=request.session.get('user')
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                status=True
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
                mob=request.session['mobile']=userid.mobile

                #OTP Sending 
                """otp=random.randint(1111,9999)
                url = "https://www.fast2sms.com/dev/bulkV2"
                querystring = {"authorization":"KEodGZf5czOeCxJPkWAFHQUYtS86Rbmrv1MyuViag4hs7N2DujvzKSw5MN9mRryb3LC4DsIHiWph78","variables_values":f"{otp}","route":"otp","numbers":f"{mob}"}
                headers = {
                    'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)"""

                return redirect('notes')
            else:
                print("Error! Username or Password invalid...")
    return render(request,'index.html',{'cuser':cuser,'st':status})

def notes(request):
    cuser=request.session.get('user')
    if request.method=='POST':
        newnotes=notesForm(request.POST,request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Your notes has been submitted!")
        else:
            print(newnotes.errors)
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
    if request.method=='POST':
        newCallback=callbackForm(request.POST)
        if newCallback.is_valid():
            newCallback.save()
            print("Your form has been submitted!")

            #Email Sending Code
            sub="Thank you!"
            msg=f"Hello User!\n\nWe have recieved your feedback, We will contact you in short time.\n\nThanks & regards!\nNotesApp Team\n+91 9724799469 | help@notesapp.com"
            from_ID=settings.EMAIL_HOST_USER
            #to_ID=["nehagaraniya360@gmail.com","sanjuahir009@gmail.com","parmarmayur5778@gmail.com","divyeshpatel6825@gmail.com"]
            to_ID=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
        else:
            print(newCallback.errors)
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect('/')
