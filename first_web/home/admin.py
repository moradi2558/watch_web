from django.contrib import admin
from .models import*

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','create','update')
    list_filter  = ('create',)
    prepopulated_fields = {'slug':('name',)}
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','create','update','available','amount','unit_price','discount','total_price']
    list_filter = ('available',)
    
    
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)