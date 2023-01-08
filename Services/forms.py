from django import forms
from .models import ListClients

class ClientContactForm(forms.ModelForm):

    class Meta:

        model = ListClients
        fields = [
            'first_name',
            'second_name'
            'phone',
            'email',
        ]