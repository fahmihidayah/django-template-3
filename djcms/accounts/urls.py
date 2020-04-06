from django.contrib import admin
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.AccountLoginView.as_view(), name='account_login'),
]