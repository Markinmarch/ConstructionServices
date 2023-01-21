from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response

def intro(request):
    return render(request, 'begin.html')

@api_view(['GET'])
def demo(request):
    data = {'massage':'Hello'}
    return Response(data)