from django.contrib import admin
from . models import*
from django_jalali.admin.filters import JDateFieldListFilter
# Register your models here.
class ItemInline(admin.TabularInline):
    '''Tabular Inlinew for '''
    model = ItemOrder
    readoly_fields = ['user','product','variant','quantity','size','price']
    
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user','email','f_name','l_name','address','create','paid','get_price','code'
    ]
    list_filter = (
        ('code',JDateFieldListFilter),
    )
    inlines = [ItemInline]
    
class CouponAdmin(admin.ModelAdmin):
    list_display = [
        'code','start','end','discount','active'
    ]


admin.site.register(Order,OrderAdmin)
admin.site.register(ItemOrder)
admin.site.register(Coupon,CouponAdmin)