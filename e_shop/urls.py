# e_shop URL Configuration


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.home.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('apps.product.urls')),
    path('user/', include('apps.user.urls')),
    path('', index , name='home'),
    path('i18n/',include('django.conf.urls.i18n')),
]

# urlpatterns += i18n_patterns(
#     path('' ,include('apps.product.urls'))
# )



urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

