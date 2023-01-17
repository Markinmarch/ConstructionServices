from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response

def intro(request):
    return render(request, 'begin.html')

def registration(request):
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = UserCreationForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохраняем пользователя
            form.save()
            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            # Рендаринг страницы
            return render(request, 'begin.html', data)
    else: # Иначе
        # Создаём форму
        form = UserCreationForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
        return render(request, 'registration.html', data)

@api_view(['GET'])
def demo(request):
    data = {'massage':'Hello'}
    return Response(data)