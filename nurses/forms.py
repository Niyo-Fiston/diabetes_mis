# nurses/forms.py

from django import forms
from django.forms import ModelForm, widgets
from .models import Nurse

class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}), 
            'age': forms.NumberInput(attrs={'class': 'form-control'}), 
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }