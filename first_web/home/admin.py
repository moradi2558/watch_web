from django.contrib import admin
from .models import*

# Register your models here.
class ProductVariantInlines(admin.TabularInline):
    model = Variant
    extera = 2    
    
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','create','update','sub_category')
    list_filter  = ('create',)
    prepopulated_fields={'slug':('name',)}
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','create','update','available','amount','unit_price','discount','total_price',]
    list_filter = ('available',)
    inlines = [ProductVariantInlines]
    list_editable=('amount',)
    raw_id_fields = ('Category',)
    
class VariantAdmin(admin.ModelAdmin):
    list_display=['name','id']

  
class SizeAdmin(admin.ModelAdmin):
    list_display=['name','id']
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Variant)
admin.site.register(Size)
admin.site.register(Color)