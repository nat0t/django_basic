from django.contrib import admin
from django.contrib import admin
from .models import ProductsCategory, Product

# Register your models here.
admin.site.register(ProductsCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', 'short_description',
              ('price','quantity'), 'category')
    readonly_fields = ('short_description',)
    ordering = ('name', 'price')
    search_fields = ('name',)