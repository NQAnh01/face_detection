from django import forms
from .models import *
  
class detectForm(forms.ModelForm):
  
    class Meta:
        model = Detect
        fields = ['detect']