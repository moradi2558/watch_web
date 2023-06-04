from django.shortcuts import render,redirect
from home.models import Product
from.models import*
from django.contrib.auth.decorators import login_required
from order.models import*
# Create your views here.

def cart_detail(request):
    cart = Cart.objects.filter(user_id=request.user.id)
    form = OrderForm 
    total = 0
    user = request.user
    for p in cart:
        if p.product.status != 'None':
            total += p.variants.total_price*p.quantity
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