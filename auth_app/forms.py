from django import forms

from auth_app.models import CustomUser


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password',)
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter a email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter the password'}),
        }
