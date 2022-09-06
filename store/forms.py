from django import forms
from store.models import *

class uform(forms.ModelForm):
    class Meta:
        model=user
        fields="__all__"