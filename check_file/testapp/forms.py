from django import forms
from .models import FileCheck

class OurForm(forms.ModelForm):
    class Meta:
        model = FileCheck
        fields = [
            'file',
        ]