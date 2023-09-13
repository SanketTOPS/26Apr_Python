from django.contrib import admin
from .models import userSignup,callback,mynotes

# Register your models here.

class signupClass(admin.ModelAdmin):
    list_display=['id','firstname','lastname','username','city','state','mobile']

class callbackClass(admin.ModelAdmin):
    list_display=['id','fullname','email','mobile','msg']

class mynotesClass(admin.ModelAdmin):
    list_display=['id','query','opt','myfiles','comments']

admin.site.register(userSignup,signupClass)
admin.site.register(callback,callbackClass)
admin.site.register(mynotes,mynotesClass)
