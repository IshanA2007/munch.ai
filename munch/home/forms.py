# forms.py
from django import forms


class TextInputForm(forms.Form):
    text_input = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-textbox-control", "autocomplete": "off"}
        ),
    )


class ImageUploadForm(forms.Form):
    image = forms.ImageField(label="")
