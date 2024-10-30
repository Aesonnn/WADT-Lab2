# emailapp/forms.py

from django import forms
from .models import Person

# Form for sending emails
class EmailForm(forms.Form):
    email = forms.EmailField(label='Recipient Email', required=False)
    subject = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email']