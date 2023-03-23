from django import forms
from .models import Movielist

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Movielist
        fields = ['name','year','desc','img']
