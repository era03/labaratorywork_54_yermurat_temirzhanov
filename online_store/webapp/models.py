from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=200, null=False, blank=False, verbose_name='Категория')
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание категории')

    def __str__(self) -> str:
        return f'{self.category}'


class Product(models.Model):
    category = models.ForeignKey (
        verbose_name = 'Категория',
        to = 'webapp.Category',
        null = False,
        blank = False,
        related_name = 'products',
        on_delete = models.RESTRICT
    )
    product = models.CharField(max_length=200, null=False, blank=False, verbose_name='Продукт')
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    product_image =  models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание категории')
    
    def __str__(self) -> str:
        return f'{self.product} - {self.price} - {self.created_at}'
