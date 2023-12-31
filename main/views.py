from django.shortcuts import render
# Create your views here.

def index(request):
    context: dict[str, str] = {
        'title': 'Home  - Главная',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context: dict[str, str] = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'textOnPage': 'Кокрейн - это международное сообщество со штаб-квартирой в Великобритании, зарегистрированное как некоммерческая организация, являющееся членом Национального совета добровольных организаций Великобритании.',
    }
    return render(request, 'main/about.html', context)
