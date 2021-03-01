from django.shortcuts import render
import os
from geekshop.settings import STATIC_URL
from mainapp.models import Product, ProductsCategory

dir = os.path.dirname(__file__)

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    slides = os.listdir(os.path.join(STATIC_URL[1:], 'vendor/img/slides/'))

    context = {'title': 'GeekShop - каталог',
               'slides': slides,
               'products': Product.objects.all(),
               'categories': ProductsCategory.objects.all(),
               }
    return render(request, 'mainapp/products.html', context)

