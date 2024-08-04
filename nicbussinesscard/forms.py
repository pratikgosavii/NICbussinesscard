from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.forms.widgets import DateTimeInput

        


class demo_Form(forms.ModelForm):
    class Meta:
        model = demo
        fields = '__all__'
        widgets = {
           
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'amount': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'amount'
            }),
            'remark': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'random_key'
            }),

        }

class payment_Form(forms.ModelForm):
    class Meta:
        model = payment
        fields = '__all__'
        widgets = {
           
            'demo': forms.Select(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'amount': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'amount'
            }),
            'remark': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'random_key'
            }),

            'date': DateTimeInput(attrs={'type': 'date', 'class' : 'form-control'}, format = '%Y-%m-%d'),


        }


class client_Form(forms.ModelForm):
    class Meta:
        model = client
        fields = '__all__'
        widgets = {
           
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'company_name'
            }),
            'random_key': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'random_key'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'mail': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'mobile_no': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'desigination': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'whatsapp': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control'}),
            'linkdin': forms.URLInput(attrs={'class': 'form-control'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control'}),
            'website1': forms.URLInput(attrs={'class': 'form-control'}),
            'address_link': forms.URLInput(attrs={'class': 'form-control'}),
            
           
     
            
        }
