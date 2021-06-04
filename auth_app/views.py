from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from auth_app.forms import UserForm
from auth_app.models import CustomUser


class CreateUserView(generic.CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'auth/sign-up.html'
    success_url = reverse_lazy('index-gist')


class LoginUserView(generic.View):
    form_class = UserForm
    template_name = 'auth/sign-in.html'
    success_url = reverse_lazy('index-gist')

    def get(self, request):
        context = {
            'form': self.form_class
        }
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(self.success_url)
        elif user is None:
            messages.error(request, 'username or password not correct')
            return redirect('sign-in')
        else:
            messages.error(request, 'some problems in server, sorry')
            return redirect('sign-in')

