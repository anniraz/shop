from django.urls import path

from apps.product.views import *


urlpatterns = [
    path('', homepageview, name='homepage'),
    # path('register/',RegisterUser.as_view(), name='register'),
    # path('login/',LoginUser.as_view(),name='login'),
    # path('logout/', logout_user, name='logout'),
    path('product_detail/<int:id>/',product_detail,name='product_detail'),
    path('category detail/<int:id>/',categoryDetail,name='category'),
    path('products/',products),


    
]



