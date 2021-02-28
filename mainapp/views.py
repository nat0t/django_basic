from django.shortcuts import render
import json
import os
from geekshop.settings import STATIC_URL

dir = os.path.dirname(__file__)

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    slides = os.listdir(os.path.join(STATIC_URL[1:], 'vendor/img/slides/'))
    json_path = os.path.join(dir, 'fixtures/products.json')
    with open(json_path) as db:
        data = json.load(db)

    context = {'title': 'GeekShop - каталог',
               'topics': ('Новинки', 'Одежда', 'Обувь', 'Аксессуары',
                          'Подарки'),
               'slides': slides,
               'data': data,
               }
    return render(request, 'mainapp/products.html', context)

