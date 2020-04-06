from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class AccountLoginView(TemplateView):
    template_name = "accounts/login.html"

