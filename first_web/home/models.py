from django.db import models
from accounts.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 200)
    create = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to = 'Category')

    def __str__(self):
        return self.name


class Product(models.Model):
    Category = models.ForeignKey(Category,on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    amount = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField(blank = True,null = True)
    information = models.TextField(blank = True,null = True)
    create = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to = 'product')
    available = models.BooleanField(default = True)
    
    def __str__(self):
        return self.name

    
    
    
    @property
    def total_price(self):
        if not self.discount:
            return self.unit_price
        elif self.discount:
            total = (self.discount*self.unit_price)/100
            return int(self.unit_price - total)
        return self.total_price