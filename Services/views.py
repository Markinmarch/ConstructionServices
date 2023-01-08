from django.shortcuts import redirect, render, HttpResponse

# from .models import Client

# Create your views here.

def intro(request):
   return render(request, 'begin.html')

def registration(request):
   return render(request, 'register.html')
   # return HttpResponse(print('REGISTRATION'))