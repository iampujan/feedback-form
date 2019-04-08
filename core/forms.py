from django import forms

class FBForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()