from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'
urlpatterns = [
    path('',views.home,name = 'home'),
    path('product/',views.all_product,name = 'product'),
    path('detail/<int:id>/',views.product_detail,name ='detail'),
    path('category/<int:id>/',views.all_product,name ='category'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)