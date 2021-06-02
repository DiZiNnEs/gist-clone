from django.urls import reverse, reverse_lazy
from django.views import generic

from auth_app.forms import UserForm
from auth_app.models import CustomUser


class CreateUserView(generic.CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'auth/sign-up.html'
    success_url = reverse_lazy('sign-in')


class LoginUserView(generic.FormView):
    form_class = UserForm
    template_name = 'auth/sign-in.html'
    success_url = '/'
