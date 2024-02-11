# forms.py
from django import forms

class TextInputForm(forms.Form):
    text_input = forms.CharField(label='Enter text')

class ImageUploadForm(forms.Form):
    image = forms.ImageField()