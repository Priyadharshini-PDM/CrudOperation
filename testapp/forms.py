from django import forms
from django.forms import ModelForm
from .models import company

class Employees_form(ModelForm):
    class Meta:
        model=company
        fields=('emp_name','emp_email','emp_role','emp_contact','emp_salary')
        widgets = {
            'emp_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'emp_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'emp_contact': forms.TextInput(attrs={'size':10,'class': 'form-control', 'placeholder': 'Contact No.'}),
            'emp_role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Role'}),
            'emp_salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            }
