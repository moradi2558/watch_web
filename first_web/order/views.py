from django.shortcuts import render,redirect
from cart.models import*
from .models import*
from .forms import CouponForm
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.contrib import messages
from suds import Client
from django.http import HttpResponse
import jdatetime
from django.utils.crypto import get_random_string 
# Create your views here.
def order_detail(request,order_id):
    order = Order.objects.get(id=order_id)
    form_order = CouponForm()
    context = {'order':order,'form_order':form_order }
    return render(request,'order/order.html',context)

def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            code = get_random_string
            order = Order.objects.create(user_id=request.user.id,email=data['email'],f_name=data['f_name'],
                                         l_name=data['l_name'],address=data['address'],code = code )
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
        time = jdatetime.datetime.now()
        try:
           coupon = Coupon.objects.get(code__iexact = code,start__lte = time,end__gte = time,active = True) 
        except Coupon.DoesNotExist:
            messages.error(request,'wrong code','danger')
            return redirect('order:order_detail',order_id)
        order = Order.objects.get(id=order_id)
        order.discount = coupon.discount 
        order.save()
    return  redirect('order:order_detail',order_id)

MERCHANT = '?????'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
mobile = '09123456789'  # Optional
CallbackURL = 'http://localhost:8000/order:verify/'  # Important: need to edit for realy server.


def send_request(request,order_id,price):
        global amount,id
        amount = price 
        id = order_id
        result = client.service.PaymentRequest(MERCHANT,amount, description,
                                               request.user.email, mobile, CallbackURL)
        if result.Status == 100:
            return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
        else:
            order = Order.objects.get(id = id)
            order.paid = True
            order.save()
            cart = ItemOrder.objects.filter(order_id = id)
            for c in cart:
                if Product.status == 'None':
                    products = Product.objects.get(id = c.product.id)
                    products.amount -= c.quantity
                    products.save()
                else: 
                    variant = Variant.objects.get(id = c.variant.id)
                    variant.amount -= c.quantity
                    variant.sell += c.quantity
                    variant.save()
            return HttpResponse('Error code: ' + str(result.Status))


def verify(request):
        if request.GET.get('Status') == 'OK':
            result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
            if result.Status == 100:
                order.paid = True
                order.save()
                cart = ItemOrder.objects.filter(order_id = id)
                for c in cart:
                    if product.status == 'None':
                        product = Product.objects.get(id = c.product.id)
                        product.amount -= c.quantity
                        product.save()
                    else: 
                        variant = Variants.objects.get(id = c.variant.id)
                        variant.amount -= c.quantity
                        variant.save()
                return render(request, 'order/success.html', {'order': order})
            elif result.Status == 101:
                return render(request, 'order/error.html')
            else:
                return render(request, 'order/error.html')
        else:
            return render(request, 'order/error.html')
