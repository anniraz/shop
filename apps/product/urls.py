from django.urls import path

from apps.product.views import homepageview,product_detail,categoryDetail,products


urlpatterns = [
    path('', homepageview, name='homapage'),
    path('product_detail/<int:id>/',product_detail,name='product_detail'),
    path('category detail/<int:id>/',categoryDetail,name='category'),
    path('products/',products),

    
]



