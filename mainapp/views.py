from django.shortcuts import render
from django.core.paginator import Paginator
import os

from geekshop.settings import STATIC_URL
from mainapp.models import Product, ProductsCategory

dir = os.path.dirname(__file__)

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None):
    slides = os.listdir(os.path.join(STATIC_URL[1:], 'vendor/img/slides/'))

    context = {'title': 'GeekShop - каталог',
               'slides': slides,
               'categories': ProductsCategory.objects.all(),
               }
    if category_id:
        context.update(
            {'products': Product.objects.filter(category_id=category_id)}
        )
    else:
        context.update({'products': Product.objects.all()})
    return render(request, 'mainapp/products.html', context)