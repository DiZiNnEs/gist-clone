from django import forms

from auth_app.models import CustomUser


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password',)
