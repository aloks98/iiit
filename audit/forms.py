from django import forms
from django.forms import ModelForm

from audit.models import *


class SocForm(ModelForm):
    class Meta:
        model = Society
        fields = '__all__'


class SecForm(ModelForm):
    class Meta:
        model = Secretaries
        fields = '__all__'


class PropForm(ModelForm):
    class Meta:
        model = Proposals
        fields = '__all__'
