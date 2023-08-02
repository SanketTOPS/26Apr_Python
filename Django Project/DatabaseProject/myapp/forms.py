from django import forms
from .models import userInfo

class userForm(forms.ModelForm):
    class Meta:
        model=userInfo
        fields='__all__'


class updateData(forms.ModelForm):
    class Meta:
        model=userInfo
        fields=['firstname','lastname','email','dob','mobile']