from django import forms

from .models import *
from django.contrib.admin.widgets import  AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

        


class client_Form(forms.ModelForm):
    class Meta:
        model = client
        fields = '__all__'
        widgets = {
           
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
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
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control'}),
            'website1': forms.URLInput(attrs={'class': 'form-control'}),
            
           
     
            
        }
