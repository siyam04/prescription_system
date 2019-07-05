from django import forms
from django.forms import TextInput, Select, SelectDateWidget, TimeInput, NumberInput

from .models import Prescription


class PrescriptionAddForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient_name', 'patient_age', 'patient_gender', 'diagnosis', 'medicines',
                  'prescription_date', 'next_visit_date', 'user']

        widgets = {
            'patient_name': TextInput(attrs={'class': 'form-control'}),
            'patient_age': NumberInput(attrs={'class': 'form-control'}),
            'patient_gender': Select(attrs={'class': 'form-control'}),
            'diagnosis': TextInput(attrs={'class': 'form-control'}),
            'medicines': TextInput(attrs={'class': 'form-control'}),
            'prescription_date': SelectDateWidget(attrs={'class': 'form-control'}),
            'next_visit_date': SelectDateWidget(attrs={'class': 'form-control'}),
        }
