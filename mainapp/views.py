from django.shortcuts import render
import json
import os
from geekshop.settings import STATIC_URL
from mainapp.models import Product, ProductsCategory

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
               'slides': slides,
               'data': data,
               'products': Product.objects.all(),
               'categories': ProductsCategory.objects.all(),
               }
    return render(request, 'mainapp/products.html', context)

