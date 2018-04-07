# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from darice.models import Product
from .forms import UserCreateForm


class MainView(TemplateView):
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            products = Product.objects.all()
            ctx = {'products': products}
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})


class RegisterFormView(FormView):
    form_class = UserCreateForm
    template_name = 'register.html'
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()     # recieving of user's object
        login(self.request, self.user)  # authenticating of user
        return super(LoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginFormView, self).form_invalid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
