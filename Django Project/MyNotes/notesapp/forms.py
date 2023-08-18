from django import forms
from .models import userSignup


class signupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'
    
class updateForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields=['firstname','lastname','username','password','state','city','mobile']