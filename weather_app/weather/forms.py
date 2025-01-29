from django import forms

class CityForm(forms.Form):
    city = forms.CharField(
        label="Enter your city",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter city name'
        })
    )
