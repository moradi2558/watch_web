from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from.forms import *
from django.db.models import Q
from cart.models import*
from django.core.mail import EmailMessage 
# Create your views here.


def home(request):
    category = Category.objects.filter(sub_cat=False)
    return render(request, 'home.html', {'category': category})


def all_product(request, slug=None, id=None):
    products = Product.objects.all()
    category = Category.objects.filter(sub_cat=False)
    form = SearchForm()
    if 'search' in request.GET:
         form = SearchForm(request.GET)
         if form.is_valid():
            data = form.cleaned_data['search']
            if data is not None:
                product = products.filter(Q(name__contain = data))
    if slug and id:
        data = get_object_or_404(Category, slug=slug, id=id)
        products = products.filter(Category=data)
    return render(request, 'product.html', {'products': products, 'category': category,'form':form})


def product_detail(request,id):
    products = get_object_or_404(Product,id=id)
    comment_form = CommentForm()
    comment = Comment.objects.filter(product_id = id,is_reply = False)
    similar = products.tags.similar_objects()[:2]
    cart_form = CartForm()
    image =Images.objects.filter(product_id = id)
    is_like=False
    is_favourite = False 
    if products.favourite.filter(id=request.user.id).exists():
        is_favourite = True  
    reply_form = ReplyForm()
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
                   'variants': variants, 'similar': similar,'is_like':is_like,'is_unlike':is_unlike,
                   'comment':comment,'comment_form':comment_form,'reply_form':reply_form,'image':image,
                   'cart_form':cart_form,'is_favourite':is_favourite}
        return render(request,'detail.html',context)
    else:
        return render(request,'detail.html',{'products': products,'similar': similar,'is_like':is_like,
                                             'reply_form':reply_form,'cart_form':cart_form,'is_unlike':is_unlike,
                                             'comment':comment,'comment_form':comment_form,'image':image
                                             ,'is_favourite':is_favourite})
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
 
 
def product_reply(request,id,comment_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            data = reply_form.cleaned_data
            Comment.objects.create(comment = data['comment'], product_id = id,user_id = request.user.id , reply_id = comment_id,is_reply = True)
            messages.success(request,"success","success")
            return redirect(url)
           
def comment_like(request,id):
    url = request.META.get('HTTP_REFERER')
    comment=Comment.objects.get(id=id)
    if comment.comment_like.filter(id=request.user.id).exists():
        comment.comment_like.remove(request.user)
    else:
        comment.comment_like.add(request.user)
        messages.success(request,"success","success")
    return redirect(url)
        
        
def product_search(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['search']
            if data.isdigit():
                products = products.filter(Q(discount__exact = data)|Q(unit_price__exact = data))
            else:
                products = products.filter(Q(name__icontains = data))
            return render (request,'product.html',{'products':products,'form':form})
        
def favourie_product(request,id):
    product = Product.objects.get(id=id)
    url = request.META.get('HTTP_REFERER') 
    is_favourite=False 
    if product.favourite.filter(id=request.user.id).exists():
        product.favourite.remove(request.user)
        is_favourite = False 
    else:
        product.favourite.add(request.user)
    return redirect (url)

def contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        msg = request.POST['message']
        body = subject + '\n' + email + '\n' + msg 
        form = EmailMessage(
            'contact us',
            body,
            'test',
            ('25mohamad25582@gmail.com',)
        )
        form.send(fail_silently = False)
    return render(request,'contact.html')