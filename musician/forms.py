from django import forms 
from .models import Musician

class MusicianForm(forms.ModelForm):
    class Meta:
        model=Musician
        fields='__all__'

        labels={
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'Email',
            'number':'Contact',
            'instrument':'Instrument'
        }

        help_texts={
             'first_name':'Enter Your First Name',
            'last_name':'Enter Your Last Name',
            'email':'Enter Your Email',
            'number':'Enter Your Contact',
            'instrument':'Enter Your Instrument Name'
        }

        def clean(self):
            clean_data = super().clean()
            first_name = clean_data.get('first_name')
            last_name = clean_data.get('last_name')
            email = clean_data.get('email')
            number = clean_data.get('number')

            if (first_name and first_name.isdigit()) or (last_name and last_name.isdigit()):
                raise forms.ValidationError('User name cannot be number')
            if number and len(str(number)) != 11:
                raise forms.ValidationError('Number must be 11 digits')
            if email and '@gmail.com' not in email:
                raise forms.ValidationError('Please provide a valid email')

            return clean_data
