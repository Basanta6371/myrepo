from django import forms
from .models import EmpData

class EmpForm(forms.ModelForm):
    class Meta:
        model = EmpData
        fields = ['name','salary','company']


