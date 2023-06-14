from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
import sys

# Create your views here.

def index(request):
    return render(request,'chips.html')