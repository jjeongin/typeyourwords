from django import forms
from .models import Word
from django.forms import HiddenInput

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word',]