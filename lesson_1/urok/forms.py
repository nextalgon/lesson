from django import forms


class TextForm(forms.Form):
    name = forms.CharField(label='ismingiz', max_length=50)
    surname = forms.CharField(label='familyangiz', max_length=50)
