from django.shortcuts import render
import json
import os, os.path
from geekshop.settings import STATIC_URL

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    slides_dir = os.path.join(STATIC_URL[1:], 'vendor/img/slides/')
    slides = os.listdir(slides_dir)
    slides = [os.path.join(slides_dir, slide) for slide in slides]

    with open('mainapp/fixtures/products.json') as db:
        data = json.load(db)

    context = {'title': 'GeekShop - каталог',
               'topics': ('Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки'),
               'slides': slides,
               'data': data,
               }
    return render(request, 'mainapp/products.html', context)

