from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search Books', max_length=100)
