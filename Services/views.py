from django.shortcuts import redirect, render, HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages

# from .models import Client

# Create your views here.

def intro(request):
   return render(request, 'begin.html')

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Создан аккаунт {username}')
        return redirect('home')
    else:
        form = UserRegisterForm()
        return render(request, 'registration.html', {'form': form})