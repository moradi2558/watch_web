from django.db import models
from accounts.models import User
from django.urls import reverse
from  ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager 
from django.forms import ModelForm
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode = True,unique= True,null=True,blank = True)
    image = models.ImageField(upload_to='Category',null=True, blank=True)
    sub_category = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub')
    sub_cat = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("home:category", args=[self.slug,self.id])
    

class Product(models.Model):
    Category = models.ManyToManyField(Category, blank=True)
    VARIANT = (('None', 'none'),
               ('Size', 'size'),
               ('Color', 'color'),
    )
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField(blank=True, null=True)
    information = RichTextUploadingField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    tags = TaggableManager(blank=True)
    status = models.CharField(
        max_length=200, blank=True, null=True, choices=VARIANT)
    image = models.ImageField(upload_to='product')
    available = models.BooleanField(default=True)
    like = models.ManyToManyField(User,blank = True,related_name = 'product_like')
    total_like = models.IntegerField(default=0)
    unlike = models.ManyToManyField(User,blank = True,related_name = 'product_unlike')
    total_unlike = models.IntegerField(default=0)
    
    def total_like(self):
        return self.like.count()
    def total_unlike(self):
        return self.unlike.count()
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home:detail', args=[self.id])

    @property
    def total_price(self):
        if not self.discount:
            return self.unit_price
        elif self.discount:
            total = (self.discount*self.unit_price)/100
            return int(self.unit_price - total)
        return self.total_price



class Size(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
class Color(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
class Variant(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    product_variant = models.ForeignKey(Product,on_delete = models.CASCADE)
    size_variant = models.ForeignKey(Size,on_delete = models.CASCADE,null = True,blank = True)
    color_variant = models.ForeignKey(Color,on_delete = models.CASCADE,null = True,blank = True)
    amount = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField(blank=True, null=True)
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
    
    
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    comment = models.TextField()
    rate = models.PositiveIntegerField(default = 1)
    create = models.DateTimeField(auto_now_add = True)
    reply = models.ForeignKey('self' , on_delete = models.CASCADE,blank = True,null = True ,related_name = 'comment_reply')
    is_reply = models.BooleanField(default = False)
    comment_like = models.ManyToManyField(User,blank = True,related_name = 'com_like')
    total_comment_like = models.PositiveIntegerField(default = 0)
    
    def total_like_comment(self):
        return self.comment_like.count()
        
    def __str__(self):
        return self.product.name
    
    
class CommentForm(ModelForm):
    class Meta : 
        model = Comment
        fields = ['comment' , 'rate'] 
        
        
        
class ReplyForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']           