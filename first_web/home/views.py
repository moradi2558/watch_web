from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.


def home(request):
    category = Category.objects.filter(sub_cat=False)
    return render(request, 'home.html', {'category': category})


def all_product(request, slug=None, id=None):
    products = Product.objects.all()
    category = Category.objects.filter(sub_cat=False)
    if slug and id:
        data = get_object_or_404(Category, slug=slug, id=id)
        products = products.filter(Category=data)
    return render(request, 'product.html', {'products': products, 'category': category})


def product_detail(request,id):
    products = get_object_or_404(Product,id=id)
    comment_form = CommentForm()
    comment = Comment.objects.filter(product_id = id,is_reply = False)
    similar = products.tags.similar_objects()[:2]
    is_like=False
    if products.like.filter(id=request.user.id).exists():
        is_like=True
    is_unlike=False
    if products.unlike.filter(id=request.user.id).exists():
        is_unlike=True
    if products.status != 'None':
        if request.method == "POST":
            variant = Variant.objects.filter(product_variant_id=id)
            var_id = request.POST.get('select')
            variants = Variant.objects.get(id=var_id)
        else:
            variant = Variant.objects.filter(product_variant_id=id)
            variants = Variant.objects.get(id=variant[0].id)
        context = {'products': products, 'variant': variant,
                   'variants': variants, 'similar': similar,'is_like':is_like,'is_unlike':is_unlike,'comment':comment,'comment_form':comment_form}
        return render(request,'detail.html',context)
    else:
        return render(request,'detail.html',{'products': products,'similar': similar,'is_like':is_like,'is_unlike':is_unlike,'comment':comment,'comment_form':comment_form})
def product_like(request,id):
    url = request.META.get('HTTP_REFERER')
    product=get_object_or_404(Product,id=id)
    is_like=False
    if product.like.filter(id=request.user.id).exists():
        product.like.remove(request.user)
        is_like=False
        messages.success(request,'removed','danger')
    else:
        product.like.add(request.user)
        is_like=True
        messages.success(request,'added','success')
    return redirect(url)



def product_unlike(request,id):
    url = request.META.get('HTTP_REFERER')
    product=get_object_or_404(Product,id=id)
    is_unlike=False
    if product.unlike.filter(id=request.user.id).exists():
        product.unlike.remove(request.user)
        is_unlike=False
        messages.success(request,'removed','danger')
    else :
        is_unlike=True
        product.unlike.add(request.user)
        messages.success(request,"added","success")
    return redirect(url)


def product_comment(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            Comment.objects.create(comment=data['comment'],rate=data['rate'],user_id=request.user.id,product_id=id)
            messages.success(request,"success","success")
        return redirect(url)
        