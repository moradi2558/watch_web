from django.shortcuts import render,get_object_or_404
from .models import *
from django.http import HttpResponse
# Create your views here.



def home(request):
    category = Category.objects.all()
    return render(request, 'home.html', {'category': category})


def all_product(request,slug=None ,id=None):
    products = Product.objects.all()
    category = Category.objects.all()
    if slug and id:
        data = get_object_or_404(Category,slug=slug,id=id)
        products = products.filter(Category=data)
    return render(request, 'product.html', {'products': products, 'category': category})


def product_detail(request,slug,id):
    product = get_object_or_404(Product,slug=slug,id=id)
    return render(request, 'detail.html', {'product': product})
