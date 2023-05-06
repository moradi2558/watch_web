from django.shortcuts import render,redirect
from cart.models import*
from .models import*
from .forms import CouponForm
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.contrib import messages
# Create your views here.
def order_detail(request,order_id):
    order = Order.objects.get(id = order_id)
    form_order = CouponForm()
    context = {'order':order,'form_order':form_order }
    return render(request,'order/order.html',context)

def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            order = Order.objects.create(user_id=request.user.id,email=data['email'],f_name=data['f_name'],
                                         l_name=data['l_name'],address=data['address'])
            cart = Cart.objects.filter(user_id = request.user.id)
            for c in cart:
                ItemOrder.objects.create(order_id = order.id,user_id = request.user.id,
                                         product_id = c.product_id,variant_id = c.variants_id,quantity = c.quantity)
            return redirect('order:order_detail',order.id)
        
@require_POST
def coupon_order(request,order_id):
    form = CouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        time = timezone.now()
        try:
           coupon = Coupon.objects.get(code__iexact = code,start__lte = time,end__gte = time,active = True) 
        except Coupon.DoesNotExist:
            messages.error(request,'wrong code','danger')
            return redirect('order:order_detail',order_id)
        order = Order.objects.get(id=order_id)
        order.discount = coupon.discount 
        order.save()
    return  redirect('order:order_detail',order_id)