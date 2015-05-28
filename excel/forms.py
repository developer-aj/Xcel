from django import forms

class XlsForm(forms.Form):
    xfile = forms.FileField(label='Upload xls file')
