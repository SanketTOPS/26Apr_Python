from django import forms
from .models import userInfo

class userForm(forms.ModelForm):
    class Meta:
        model=userInfo
        fields='__all__'
