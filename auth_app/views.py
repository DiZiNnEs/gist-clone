from django.shortcuts import render
from django.views import generic

from auth_app.forms import UserForm
from auth_app.models import CustomUser


class CreateUserView(generic.CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'auth/sign-up.html'
    success_url = '/'  # change to login
