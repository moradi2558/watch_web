from django.contrib import admin
from . models import*
# Register your models here.
class ItemInline(admin.TabularInline):
    '''Tabular Inlinew for '''
    model = ItemOrder
    readoly_fields = ['user','product','variant','quantity','size']
    
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user','email','f_name','l_name','address','create','paid'
    ]
    inlines = [ItemInline]
    
admin.site.register(Order,OrderAdmin)
admin.site.register(ItemOrder)