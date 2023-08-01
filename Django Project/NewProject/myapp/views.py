from django.shortcuts import render,HttpResponse
import random

# Create your views here.
def index(request):
    return render(request,'index.html',{'name':'Ashok'}) #context

def about(request):
    nm={'name':'Nirav'}
    return render(request,'about.html',nm)

def contact(request):
    num={'num':random.randint(1111,9999)}
    return render(request,'contact.html',num)