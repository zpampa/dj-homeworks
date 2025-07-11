from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    now = datetime.datetime.now()
    return HttpResponse(f"Текущее время: {now.strftime('%Y-%m-%d %H:%M:%S')}")


def workdir_view(request):
    files = os.listdir(os.getcwd())
    files_list = '<br>'.join(files)
    return HttpResponse(f"Содержимое рабочей директории:<br>{files_list}")
