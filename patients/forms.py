# patients/forms.py

#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, Submit

from django import forms
from django.forms import ModelForm, widgets
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'last_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'glucose_level': forms.NumberInput(attrs={'class': 'form-control'}),
            'treatment_plan': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class PatientSearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

class UpdatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'glucose_level': forms.NumberInput(attrs={'class': 'form-control'}),
            'treatment_plan': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
        }