from django import forms
# from .models import ListClients
from django.contrib.auth.models import User

class ClientContactForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = [
            'first_name',
            # 'second_name'
            # 'phone',
            'email',
        ]

    def password_is_succefull(self):

        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Password do not match.')
        return cd['reteat_password']