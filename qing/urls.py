from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('mentor/', include('mentor.urls', namespace='mentor')),
    path('', include('etc.urls', namespace='etc')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('accounts/',include('accounts.urls', namespace='accounts')),
    path('accounts/', include('allauth.urls')),
    path('select2/', include('django_select2.urls')),
    path('', include('seo.urls', namespace='seo')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)