from django.core import validators
from django import forms
from .models import info

class information(forms.ModelForm):
    class Meta:
        model=info
        fields=['end_year','topic','sector','region','pestle','source','country']
        
        
        widgets={
            
            'end_year': forms.TextInput(attrs={'class':'form-control'}),
            'topic': forms.TextInput(attrs={'class':'form-control'}),
            'sector': forms.TextInput(attrs={'class':'form-control'}),
            'region': forms.TextInput(attrs={'class':'form-control'}),
            'pestle': forms.TextInput(attrs={'class':'form-control'}),
            'source': forms.TextInput(attrs={'class':'form-control'}),
            'country': forms.TextInput(attrs={'class':'form-control'}),
            
        }
        
