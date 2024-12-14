from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    text = forms.TextInput()

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'text']