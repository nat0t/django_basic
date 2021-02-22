from django.shortcuts import render
import json

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    with open('mainapp/fixtures/products.json') as db:
        data = json.load(db)

    context = {'title': 'GeekShop - каталог',
               'topics': ('Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки'),
               'sliders': {'number': 3},
               'data': data,
               }
    return render(request, 'mainapp/products.html', context)