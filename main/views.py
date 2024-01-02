from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories
# Create your views here.

def index(request):

    categories = Categories.objects.all()

    context: dict[str, str] = {
        'title': 'Home  - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories,
    }
    return render(request, 'main/index.html', context)

def about(request):
    context: dict[str, str] = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'textOnPage': 'Кокрейн - это международное сообщество со штаб-квартирой в Великобритании, зарегистрированное как некоммерческая организация, являющееся членом Национального совета добровольных организаций Великобритании.',
    }
    return render(request, 'main/about.html', context)
