from django.db import models

class Product(models.Model):
    producer = models.CharField(max_length=200)
    price = models.IntegerField()
    name = models.CharField(max_length=100, unique=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

    class __Meta__:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    class __Meta__:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name