from django.urls import path
from. import views
app_name = 'order'

urlpatterns =[
    path('<int:order_id>/',views.order_detail,name='order_detail'),
    path('order_create/',views.order_create,name ='order_create'),
]