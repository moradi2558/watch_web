from django import forms

#forms
class SearchForm(forms.Form):
    search = forms.CharField(max_length = 100)