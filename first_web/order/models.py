from django.db import models
from django.contrib.auth.models import User
from home.models import *
from django.forms import ModelForm
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    discount = models.PositiveIntegerField(null = True,blank = True)
    create = models.DateField(auto_now_add =True)
    paid = models.BooleanField(default = False)
    email = models.EmailField()
    f_name = models.CharField(max_length=300) 
    l_name = models.CharField(max_length=300) 
    address = models.CharField(max_length=1000)  
    
    def __str__(self):
        return self.user.username
    
    def get_price(self):
        total = sum(i.price()for i in self.order_item.all())
        if self.discount:
            discount_price = (self.discount/100)* total
            return int(total-discount_price)
        return total
        
class ItemOrder(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    variant = models.ForeignKey(Variant,on_delete = models.CASCADE,null =True,blank = True)
    order =  models.ForeignKey(Order,on_delete = models.CASCADE,related_name = 'order_item')
    quantity = models.IntegerField()
    
    def price(self):
        if self.product.status != 'None':
            return self.variant.total_price * self.quantity
        else:
            return self.product.total_price * self.quantity
        
    def __str__(self):
        return self.user.username
    
    def size(self):
        return self.variant.size_variant.name
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'email','f_name','l_name','address'
        ]
        
class Coupon(models.Model):
    code = models.CharField(max_length=100, unique = True)
    active = models.BooleanField(default = False)
    start = models.DateTimeField()
    end = models.DateTimeField()
    discount = models.IntegerField()