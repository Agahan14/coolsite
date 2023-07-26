from django.shortcuts import render
from django.http import HttpResponse
from women.models import Women

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Women.objects.all()
    data = {'menu': menu, 'title': 'Главная страница', 'posts': posts}
    return render(request, "index.html", data)


def about(request):
    # posts = Women.objects.all()
    data = {'menu': menu, 'title': 'О сайте'}
    return render(request, "index.html", data)
