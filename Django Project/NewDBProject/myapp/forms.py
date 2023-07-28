from django import forms
from .models import userinfo

class userdataForm(forms.ModelForm):
    class Meta:
        model=userinfo
        #fields=['firstname','lastname']
        fields='__all__'

