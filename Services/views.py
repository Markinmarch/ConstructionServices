from django.shortcuts import redirect, render, HttpResponse
from .forms import ClientContactForm

# from .models import Client

# Create your views here.

def intro(request):
   return render(request, 'begin.html')

def registration(request):
    # form = ClientContactForm(request.POST)
    # if form.is_valid(): request.method == 'POST'

    # return render(request, 'register.html')
    if request.method == 'POST':
        client_form = ClientContactForm(request.POST)
        if client_form.is_valid():
            new_client = client_form.save(commit=False)
            new_client.set_password(client_form.cleaned_data['password'])
            new_client.save()
            return render(request, 'register_done.html', {'new_client': new_client})
    else:
        client_form = ClientContactForm()
    return render(request, 'registeration.html', {'client_form':client_form})