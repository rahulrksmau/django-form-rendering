# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import DataForm


# Create your views here.

def home(request):
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            pass  # doing something with valid data
    else:
        form = DataForm()
    return render(request, 'first_page/user.html', {"form": form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            pass #do something
    else:
        form = UserCreationForm()
    return render(request, 'first_page/user.html', {'form':form})