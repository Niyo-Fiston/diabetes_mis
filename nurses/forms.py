# nurses/forms.py

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Nurse

class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = '__all__'

def __init__(self, *args, **kwargs):
        super(AddNurseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            '__all__',
            Submit('submit', 'Save Nurse')
        )