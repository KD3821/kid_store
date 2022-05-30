from django.shortcuts import render, redirect
from django.views import generic
from .models import Product, Category

def home_view(request):
    product_list = Product.objects.order_by('cat')
    context = {'product_list': product_list}
    return render(request, 'all.html', context)


def detail_view(request, name):
    item = Product.objects.get(name=name)
    context = {'item': item}
    return render(request, 'detail.html', context)


def category_view(request, cat):
    product_list = Product.objects.filter(cat__name=cat)
    context = {'product_list': product_list, 'category': cat}
    return render(request, 'all.html', context)



# class ListView(generic.ListView):
#     model = Category
#     template_name = 'shop/all.html'

