from django import forms

class ExampleForm(forms.Form):
    # Define your form fields
    example_field = forms.CharField(max_length=100, label='Example Field')
