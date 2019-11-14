from django import forms
from audit.models import *


class AuditForm(forms.ModelForm):
    class Meta:
        model = Secretaries
        widgets = {
            'password': forms.PasswordInput()
        }