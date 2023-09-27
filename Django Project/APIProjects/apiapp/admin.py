from django.contrib import admin
from .models import *


# Register your models here.
class studinfoData(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','name','email','mobile','city']

admin.site.register(studinfo,studinfoData)