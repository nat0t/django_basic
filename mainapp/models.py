from django.db import models

# Create your models here.
class ProductsCategory(models.Model):
    name = models.CharField(max_length=64, unique=True,
                            verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name_plural = 'Product categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    short_description = models.CharField(max_length=64, blank=True,
                                         verbose_name='Краткое описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0,
                                verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0,
                                           verbose_name='Количество')
    image = models.ImageField(upload_to='products_images', blank=True,
                              verbose_name='Фото')
    category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE,
                                 verbose_name='Категория')

    def __str__(self):
        return f'{self.name} | {self.category.name}'