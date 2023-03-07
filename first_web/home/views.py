from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.



def home(request):
    category = Category.objects.all()
    return render(request, 'home.html', {'category': category})


def all_product(request, id=None):
    products = Product.objects.all()
    category = Category.objects.all()
    if id:
        data = Category.objects.get(id=id)
        products = products.filter(Category=data)
    return render(request, 'product.html', {'products': products, 'category': category})


def product_detail(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'detail.html', {'product': product})
