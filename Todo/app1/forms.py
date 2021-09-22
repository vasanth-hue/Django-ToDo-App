from django import forms
from django.forms import ModelForm

from . models import *

class CreateForm(forms.ModelForm):

    class Meta:
        model = Create
        fields = '__all__'