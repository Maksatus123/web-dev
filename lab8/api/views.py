from django.shortcuts import render
from .models import *
from django.core import serializers
from django.http import HttpResponse


def show_products(request):
    data = serializers.serialize('json', Product.objects.all())
    return HttpResponse(data, content_type='application/json')


def show_product(request, pk):
    product = Product.objects.get(pk=pk)
    data = serializers.serialize('json', [product])
    return HttpResponse(data, content_type='application/json')

def show_categories(request):
    categories = serializers.serialize('json', Category.objects.all())
    return HttpResponse(categories, content_type='application/json')


def show_category(request, pk):
    category = Category.objects.get(id=pk)
    data = serializers.serialize('json', [category])
    return HttpResponse(data, content_type='application/json')

def show_list_of_products_by_category(request, pk):
    categor = Category.objects.get(id=pk)
    data = Product.objects.filter(category=categor)
    products = serializers.serialize('json', data)
    return HttpResponse(products, content_type='application/json')