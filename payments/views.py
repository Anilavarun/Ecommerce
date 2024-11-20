from django.urls import path
from django.shortcuts import render
from .models import *

def payment(request):
    return render(request,'payment.html')