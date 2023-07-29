import  django_filters
from django import forms 
from .models import* 
class ProductFilter(django_filters.FilterSet):
    Choice_1 = {
        ('expensive','expensive'),
        ('cheap','cheap'),
    }
    Choice_2 = {
        ('old','old'),
        ('new','new'),
    }
    Choice_3 = {
        ('most_discout','most discout'),
        ('less_discount','less discount')
    }
    Choice_4 = {
        ('most_sell','most sell'),
        ('less_sell','less sell'),
    }
    Choice_5 = {
        ('most_popular','most popular'),
        ('less_popular','less popular'),
    }
    price_1 = django_filters.NumberFilter(field_name = 'unit_price',lookup_expr='gte') 
    price_2 = django_filters.NumberFilter(field_name = 'unit_price',lookup_expr='lte') 
    brand = django_filters.ModelMultipleChoiceFilter(queryset = Brand.objects.all(),widget = forms.CheckboxSelectMultiple)
    color = django_filters.ModelMultipleChoiceFilter(queryset = Color.objects.all(),widget = forms.CheckboxSelectMultiple)
    size = django_filters.ModelMultipleChoiceFilter(queryset = Size.objects.all(),widget = forms.CheckboxSelectMultiple)
    price = django_filters.ChoiceFilter(choices = Choice_1,method = 'price_filter')
    create = django_filters.ChoiceFilter(choices = Choice_2,method = 'create_filter')
    discount = django_filters.ChoiceFilter(choices = Choice_3,method = 'discount_filter')
    sell = django_filters.ChoiceFilter(choices = Choice_4,method = 'sell_filter')
    django = django_filters.ChoiceFilter(choices = Choice_5,method = 'favourite_filter')
    
    
    def price_filter(self,queryset,name,value):
        data = 'unit_price' if value == 'cheap' else '-unit_price'
        return queryset.order_by(data)
    
    def create_filter(self,queryset,name,value):
        data = 'create' if value == 'old' else '-create'
        return queryset.order_by(data)
    
    def discount_filter(self,queryset,name,value):
        data = 'discount' if value == 'most_discout' else '-discount'
        return queryset.order_by(data)
    
    def sell_filter(self,queryset,name,value):
        data = 'sell' if value == 'most_sell' else '-sell'
        return queryset.order_by(data)
    
    def favourite_filter(self,queryset,name,value):
        data = 'total_favourite' if value == 'most_popular' else '-total_favourite'
        return queryset.order_by(data)