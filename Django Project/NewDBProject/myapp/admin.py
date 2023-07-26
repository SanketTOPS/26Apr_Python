from django.contrib import admin
from .models import userinfo

# Register your models here.
class userData(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','firstname','lastname','email','dob','mobile']


admin.site.register(userinfo,userData)
