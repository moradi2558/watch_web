from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'
urlpatterns = [
    path('',views.home,name = 'home'),
    path('product/',views.all_product,name = 'product'),
    path('detail/<int:id>/',views.product_detail,name ='detail'),
    path('category/<slug>/<int:id>/',views.all_product,name ='category'),
    path('like/<int:id>/',views.product_like,name='product_like'),
    path('unlike/<int:id>/',views.product_unlike,name='product_unlike'),
    path('comment/<int:id>/',views.product_comment,name = 'product_comment'),
    path('reply/<int:id>/<int:comment_id>',views.product_reply,name="product_reply"),
    path('like_comment/<int:id>',views.comment_like,name ='comment_like'),
    path('search/',views.product_search,name='product_search'),
    path('favourie/<int:id>/',views.favourie_product,name='favourite'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)