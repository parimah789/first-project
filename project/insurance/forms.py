from django import forms
from .models import Client, ClientFamily


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        exclude = ['user']

class ClientFamilyForm(forms.ModelForm):

    class Meta:
        model = ClientFamily
        exclude = ['client']