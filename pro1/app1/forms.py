from django import forms
from .models import Voters
from django.core import validators
import datetime

gen = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

class VotersForm(forms.ModelForm):
    class Meta:
        model = Voters
        fields = '__all__'

        labels = {
            'vid' : 'Voters ID',
            'fname' : 'First Name',
            'lname' : 'Last Name',
            'dob' : 'Birth Date'
        }

        widgets = {
            'vid' : forms.TextInput(attrs={'class': 'form-control'}),
            'fname' : forms.TextInput(attrs={'class': 'form-control'}),
            'lname' : forms.TextInput(attrs={'class': 'form-control'}),
            'gender' : forms.RadioSelect(choices=gen),
            'address' : forms.Textarea(attrs={'class': 'form-control', 'style': 'height:90px;'}),
            'city' : forms.TextInput(attrs={'class': 'form-control'}),
            'state' : forms.TextInput(attrs={'class': 'form-control'}),
            'pincode' : forms.TextInput(attrs={'class': 'form-control'}),
            'dob' : forms.DateInput(attrs={'type': 'date'}),
            'contact' : forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_dob(self):
        d = self.cleaned_data.get('dob')
        today = datetime.date.today()
        val = (today.year - d.year) - ((today.month, today.day) <(d.month, d.day))
        if val < 18:
            raise validators.ValidationError('Your age must be 18 or more.')
        return d