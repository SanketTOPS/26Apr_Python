from django.contrib import admin
from django.urls import path
from notesapp import views

urlpatterns = [
    path('',views.index),
    path('notes/',views.notes,name='notes'),
    path('profile/',views.profile),
    path('about/',views.about),
    path('contact/',views.contact),
    path('userlogout/',views.userlogout),
]