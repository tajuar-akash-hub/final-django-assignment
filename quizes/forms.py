from django import forms
from . models import quiz_model

class quiz_form(forms.ModelForm):
    class Meta:
        model = quiz_model
        fields = ['title','quiz_description','quiz_category','time_limit','image','quiz_banner']