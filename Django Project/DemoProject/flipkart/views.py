from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("Hello")

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')