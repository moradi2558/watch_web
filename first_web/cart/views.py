from django.shortcuts import render,redirect,get_object_or_404
from home.models import Product
from.models import*
from django.contrib.auth.decorators import login_required
from order.models import*
from django.contrib import messages
# Create your views here.

def cart_detail(request):
    cart = Cart.objects.filter(user_id=request.user.id)
    form = OrderForm
    total = 0
    user = request.user
    for p in cart:
        if p.product.status != 'None':
            total += p.variants.total_price * p.quantity
        else:
            total += p.product.total_price*p.quantity
    return render(request,'cart/cart.html',{'cart':cart,'total':total,'form':form,'user':user})


@login_required(login_url = 'accounts:login')
def add_cart(request,id):
    product = Product.objects.get(id = id)
    url = request.META.get('HTTP_REFERER')
    var_id = request.POST.get('select')
    if product.status != 'None':
        data = Cart.objects.filter(user_id = request.user.id,product_id=id,variants_id = var_id)
        if data :
            check = "yes"
        else:
            check = "no"
    else:
        data = Cart.objects.filter(user_id = request.user.id,product_id = id)
        if data :
            check = "yes"
        else:
            check = "no"
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data['quantity']
            if check == 'yes':
                if product.status != 'None':
                    shop = Cart.objects.get(user_id = request.user.id,product_id = id,variants_id = var_id)
                else :
                    shop = Cart.objects.get(user_id = request.user.id,product_id = id)
                shop.quantity += info
                shop.save()
            else:
                Cart.objects.create(user_id = request.user.id,product_id = id,variants_id = var_id,quantity = info)
        return redirect(url)
    
@login_required(login_url = 'accounts:login')
def remove_cart(request,id):
    Cart.objects.filter(id=id).delete()
    url = request.META.get('HTTP_REFERER')
    return redirect(url)

def add_single(request,id):
    url = request.META.get('HTTP_REFERER') 
    cart = Cart.objects.get(id = id)
    product = Product.objects.get(id=id)
    if cart.product.status == 'None':
        if product.amount > cart.quantity :
            cart.quantity += 1 
    else:
        variant = Variant.objects.get (id = cart.variants.id)
        if variant.amount > cart.quantity :
            cart.quantity += 1
    cart.save()
    return redirect(url)

def remove_single(request,id):
    url = request.META.get('HTTP_REFERER')
    cart = Cart.objects.get(id=id)
    if cart.quantity < 2 :
        cart.delete()
    else :
        cart.quantity -= 1 
        cart.save()
    return redirect(url)


def compare(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.user.is_authenticated :
        item = get_object_or_404(Product,id=id)
        qs = Compare.objects.filter(user_id=request.user.id,product_id=id) 
        if qs.exists():
            messages.success(request,'ok')
        else:
            Compare.objects.create(user_id=request.user.id,product_id=id,session_key=None)
    else:
        item = get_object_or_404(Product,id=id)
        qs = Compare.objects.filter(user_id=None,product_id=id) 
        if qs.exist():
            messages.success(request,'ok')
        else:
            if not request.session.session_key:
                request.session.create()
            Compare.objects.create(user_id=None,product_id=id,session_key=request.session.session_key)
    return redirect(url)

def show(request):
    if request.user.is_authenticated:
        data = Compare.objects.filter(user_id=request.user.id)
        return render(request,'cart/show.html',{'data':data})
    else:
        data = Compare.objects.filter(session_key__exact = request.session.session_key,user_id=None)
        
    
