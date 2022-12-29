from django.shortcuts import redirect, render, HttpResponse

from Services.models import Sevices

# Create your views here.

def intro(request):
   return render(request, 'begin.html')